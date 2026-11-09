"""核对外站案例隔离、生成路径和跨合集校验。"""
import copy
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from common import GENERATED_MARKER, ROOT, load_data
from build_readme import outputs, render_readme, stale_case_pages
from external_sites import is_external_site
from i18n import LANGUAGES
from source_cases import page_path, read_cases, read_external_cases, visible
from validate import read_json, validate, validate_source_cases


class ExternalSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config, cls.prompts = load_data()
        cls.primary = read_cases()
        cls.external = read_external_cases()

    def test_external_cases_only_appear_in_their_own_index_and_routes(self):
        generated = outputs(self.config, self.prompts)
        index = generated[ROOT / 'external-sites/README.md']
        primary_ids = {item['id'] for item in self.primary}
        self.assertFalse(primary_ids & {item['id'] for item in self.external})
        for item in visible(self.external):
            with self.subTest(case=item['id']):
                self.assertTrue(is_external_site(item))
                self.assertIn(page_path(item, 'zh-CN'), index)
                for language in ('en', 'zh-CN'):
                    route = page_path(item, language, external=True)
                    self.assertIn(ROOT / route, generated)
                    self.assertIn('(../../README.md#all-cases)', generated[ROOT / route])
                    self.assertNotIn(ROOT / page_path(item, language), generated)
                self.assertFalse((ROOT / 'cases' / item['id']).exists())
        for item in self.primary:
            self.assertFalse(is_external_site(item))
        for language in LANGUAGES:
            homepage = render_readme(self.config, self.prompts, language)
            self.assertIn('(external-sites/README.md)', homepage)
            for item in visible(self.external):
                self.assertNotIn(f"cases/{item['id']}/", homepage)

    def test_external_media_stays_inside_the_external_directory(self):
        errors = []
        validate_source_cases(self.config, self.external, self.prompts + self.primary,
                              errors, asset_prefix='external-sites/')
        self.assertEqual(errors, [])
        item = copy.deepcopy(next(item for item in self.external if any(media['path'] for media in item['media'])))
        media = next(media for media in item['media'] if media['path'])
        media['path'] = media['path'].removeprefix('external-sites/')
        validate_source_cases(self.config, [item], [], errors, asset_prefix='external-sites/')
        self.assertTrue(any('expected external-sites/assets/' in error for error in errors))

    def test_validation_rejects_wrong_collection_and_cross_collection_ids(self):
        original = read_json
        overrides = {'content/source-cases.json': self.primary + [self.external[0]]}

        def modified(path):
            return overrides[path] if path in overrides else original(path)

        with patch('validate.read_json', side_effect=modified):
            errors, _ = validate(check_links=False)
        self.assertTrue(any('外站来源应写入' in error for error in errors))
        self.assertTrue(any('duplicate across' in error for error in errors))
        overrides = {'external-sites/source-cases.json': self.external + [self.primary[0]]}
        with patch('validate.read_json', side_effect=modified):
            errors, _ = validate(check_links=False)
        self.assertTrue(any('应留在主合集' in error for error in errors))

    def test_stale_generated_external_pages_are_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            stale = root / 'external-sites/cases/removed/README.md'
            stale.parent.mkdir(parents=True)
            stale.write_text(GENERATED_MARKER + '\n\n已移除的案例。\n')
            manual = stale.with_name('README.manual.md')
            manual.write_text('# 手工说明\n')
            with patch('build_readme.ROOT', root):
                self.assertEqual(stale_case_pages({}), [stale])


if __name__ == '__main__':
    unittest.main()
