"""模型未知的执行记录必须如实展示，不能借来源归属断言实际模型。"""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_readme import render_case, t
from common import load_data
from validate import validate_prompts


class PromptModelProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.config, prompts = load_data()
        self.item = copy.deepcopy(prompts[0])
        self.item['model'] = {'family': None, 'variant': 'unspecified', 'api_model_id': None}

    def errors(self, item):
        errors = []
        validate_prompts(self.config, [item], errors, [], release=False)
        return errors

    def test_unknown_model_with_real_execution_and_source_is_explicitly_rendered(self):
        self.assertEqual(self.errors(self.item), [])
        for language in ('en', 'zh-CN'):
            text = render_case(self.item, self.config, language, standalone=True)
            self.assertIn(f"| {t(language, 'model_family')} | {t(language, 'unspecified')} |", text)
            self.assertNotIn('| None |', text)

    def test_unknown_family_cannot_assert_variant_or_api_model(self):
        for field, value in (('variant', 'sunburst'), ('api_model_id', 'gpt-image-2.6-sunburst')):
            with self.subTest(field=field):
                item = copy.deepcopy(self.item)
                item['model'][field] = value
                self.assertTrue(any('unverified family' in e for e in self.errors(item)))

    def test_unknown_model_requires_execution_limitations_and_source(self):
        for section, field, value in (('verification', 'status', 'source-only'), ('verification', 'notes', {'en': '', 'zh-CN': ''}), ('source', 'provenance', 'original')):
            with self.subTest(field=field):
                item = copy.deepcopy(self.item)
                item[section][field] = value
                self.assertTrue(self.errors(item))


if __name__ == '__main__':
    unittest.main()
