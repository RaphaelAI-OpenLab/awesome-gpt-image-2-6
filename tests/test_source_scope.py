"""核对保留来源、生成范围和来源限制。"""
import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_readme import outputs
from common import ROOT, load_data, published
from source_cases import is_supported_source, read_cases, visible
from validate import read_json, validate


class SourceScopeTests(unittest.TestCase):
    def test_published_cases_keep_their_bilingual_pages(self):
        config, prompts = load_data()
        cases = visible(read_cases())
        self.assertTrue(all(is_supported_source(item) for item in cases))
        generated = outputs(config, prompts)
        expected = {
            ROOT / 'cases' / item['id'] / name
            for item in cases + published(prompts) for name in ('README.md', 'README.zh-CN.md')
        }
        actual = {path for path in generated if path.name.startswith('README.')
                  and path.parent != ROOT}
        self.assertEqual(actual, expected)

    def test_source_hosts_must_match_exactly(self):
        for url in ('https://example.org/case', 'https://x.com.example.org/case'):
            with self.subTest(url=url):
                self.assertFalse(is_supported_source({'source': {'url': url}}))
        self.assertTrue(is_supported_source({'source': {'url': 'https://www.reddit.com/r/test'}}))

    def test_validation_rejects_unsupported_direct_sources(self):
        cases = copy.deepcopy(read_cases())
        cases[0]['source']['url'] = 'https://example.org/case'
        original = read_json

        def modified(path):
            return cases if path == 'content/source-cases.json' else original(path)

        with patch('validate.read_json', side_effect=modified):
            errors, _ = validate(check_links=False)
        self.assertTrue(any('本仓库仅收录' in error for error in errors), errors)


if __name__ == '__main__':
    unittest.main()
