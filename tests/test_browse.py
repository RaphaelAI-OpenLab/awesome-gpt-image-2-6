"""核对三维导航的覆盖、展开结构及准确跳转。"""
import copy
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from browse import read_browse, render_browse, validate_browse
from build_readme import render_readme
from common import load_data
from i18n import LANGUAGES, ui
from source_cases import read_cases, visible
from validate import markdown_link_errors


class BrowseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config, cls.prompts = load_data()
        cls.cases = read_cases()

    def test_all_published_cases_have_a_scene_and_valid_navigation(self):
        errors = []
        validate_browse(self.cases, errors)
        self.assertEqual(errors, [])
        expected = {item['id'] for item in visible(self.cases)}
        groups = read_browse()
        self.assertEqual([group['id'] for group in groups], ['use-cases', 'styles', 'themes'])
        actual = {case_id for item in groups[0]['items'] for case_id in item['case_ids']}
        self.assertEqual(actual, expected)

    def test_each_language_has_expandable_case_links_without_the_count_table(self):
        for language in LANGUAGES:
            with self.subTest(language=language):
                text = render_readme(self.config, self.prompts, language)
                navigation = text.split('<a id="categories"></a>', 1)[1].split('<a id="contents"></a>', 1)[0]
                self.assertNotIn('|', navigation)
                self.assertEqual(navigation.count('<details'), navigation.count('</details>'))
                self.assertEqual(navigation.count('<details'), navigation.count('<summary>'))
                for group in read_browse():
                    self.assertIn('### ' + ui(group['label']['en'], language=language), navigation)
                linked = set(re.findall(r'\]\(#source-case-([^\)]+)\)', navigation))
                expected = {item['id'] for item in visible(self.cases)}
                self.assertEqual(linked, expected)
                for case_id in linked:
                    self.assertEqual(text.count(f'<a id="source-case-{case_id}"></a>'), 1)

    def test_unknown_duplicate_and_missing_case_assignments_are_rejected(self):
        for mutation in ('unknown', 'duplicate', 'missing'):
            groups = copy.deepcopy(read_browse())
            if mutation == 'unknown':
                groups[0]['items'][0]['case_ids'].append('case-does-not-exist')
                expected = 'unknown or unpublished'
            elif mutation == 'duplicate':
                ids = groups[0]['items'][0]['case_ids']
                ids.append(ids[0])
                expected = 'duplicate case IDs'
            else:
                groups[0]['items'][0]['case_ids'].remove('docs-sailor')
                expected = 'missing cases'
            errors = []
            with patch('browse.read_browse', return_value=groups):
                validate_browse(self.cases, errors)
            self.assertTrue(any(expected in error for error in errors), (mutation, errors))

    def test_empty_or_filtered_inventories_do_not_link_missing_cases(self):
        text = render_browse([], 'zh-CN')
        self.assertEqual(text, '')
        cases = [self.cases[0]]
        text = render_browse(cases, 'zh-CN')
        self.assertIn('#source-case-' + cases[0]['id'], text)
        self.assertNotIn('#source-case-' + self.cases[1]['id'], text)

    def test_repeated_local_links_still_detect_missing_anchors(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / 'README.md').write_text(
                '<a id="existing"></a>\n\n'
                '[first](#existing)\n[second](#existing)\n[missing](#missing)\n'
            )
            with patch('validate.ROOT', root):
                errors = markdown_link_errors()
        self.assertEqual(errors, ['README.md: local anchor does not exist: #missing'])


if __name__ == '__main__':
    unittest.main()
