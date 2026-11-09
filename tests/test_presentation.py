"""Locale coverage, honest fallback, safe local badges and canonical destinations."""
import copy
import re
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from common import ROOT, load_data, localized, read_json, repo_url
from i18n import LANGUAGES, DETAIL_LANGUAGES, LANGUAGE_NAMES, filename, messages, ui
from build_readme import outputs, render_readme
from source_cases import read_cases, page_path, render_detail
from presentation import asset_outputs, language_nav, repo_badges
from validate import validate_locales


class PresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config, cls.prompts = load_data()
        cls.cases = read_cases()

    def test_sixteen_real_readme_routes(self):
        self.assertEqual(len(LANGUAGES), 16)
        self.assertEqual(len({filename(lang) for lang in LANGUAGES}), 16)
        generated = outputs(self.config, self.prompts)
        for lang in LANGUAGES:
            path = ROOT / filename(lang)
            self.assertIn(path, generated)
            self.assertEqual(path.read_text(), generated[path])

    def test_navigation_links_all_languages_and_marks_one_current(self):
        for lang in LANGUAGES:
            nav = language_nav(lang)
            self.assertEqual(len(re.findall('<a href=', nav)), 16)
            self.assertEqual(nav.count('-current.svg'), 1)
            self.assertIn(f'language-{lang}-current.svg', nav)
            for code in LANGUAGES:
                self.assertIn(f'href="{filename(code)}"', nav)
                self.assertTrue((ROOT / filename(code)).is_file())

    def test_case_details_never_map_an_unknown_language_to_chinese(self):
        for lang in LANGUAGES:
            route = page_path(self.cases[0], lang)
            expected = 'README.zh-CN.md' if lang == 'zh-CN' else 'README.md'
            self.assertTrue(route.endswith('/' + expected))
            self.assertTrue((ROOT / route).is_file())
            if lang not in DETAIL_LANGUAGES:
                with self.assertRaises(ValueError):
                    render_detail(self.cases[0], lang)
                text = render_readme(self.config, self.prompts, lang)
                notice = 'This language edition translates the repository interface. Full case details are currently available in English and Simplified Chinese.'
                self.assertIn(ui(notice, language=lang), text)

    def test_every_locale_has_all_ui_messages_and_placeholders(self):
        errors=[]
        validate_locales(errors)
        self.assertEqual(errors, [])
        for lang in LANGUAGES:
            self.assertEqual(set(messages(lang)), set(messages('en')))
            self.assertEqual(ui('Visit {brand} ↗', language=lang).count('{brand}'), 1)
        with self.assertRaises(KeyError):
            ui('This UI key has not been translated', language='ja-JP')

    def test_missing_translation_is_a_validation_error(self):
        original = read_json
        def missing(path):
            data = original(path)
            if path == 'content/locales/ja-JP.json':
                data = copy.deepcopy(data)
                del data['messages']['Languages']
            return data
        errors=[]
        with patch('validate.read_json', side_effect=missing):
            validate_locales(errors)
        self.assertTrue(any('ja-JP' in e and 'exactly match' in e for e in errors))

    def test_new_case_text_keeps_english_without_blocking_hourly_collection(self):
        text='A newly collected source description not yet translated.'
        for lang in LANGUAGES:
            self.assertEqual(localized({'en':text},lang),text)

    def test_unverified_prompt_label_is_translated_with_existing_detail_fallback(self):
        item = copy.deepcopy(self.cases[0])
        item['prompt'] = {'status': 'unverified', 'url': None}
        key = 'Prompt availability unverified'
        with patch('homepage.read_cases', return_value=[item]):
            for lang in LANGUAGES:
                with self.subTest(lang=lang):
                    translation = messages(lang)[key]
                    text = render_readme(self.config, self.prompts, lang)
                    self.assertIn(translation, text)
                    self.assertIn(page_path(item, lang), text)
                    self.assertIn(f'| {messages(lang)["Original prompts available at source"]} | **0** |', text)
                    if lang != 'en':
                        self.assertNotEqual(translation, key)
                        self.assertNotIn(key, text)

    def test_shared_anchors_and_case_inventory_are_preserved(self):
        reference = set(re.findall(r'<a id="([^"]+)"',render_readme(self.config,self.prompts,'en')))
        for lang in LANGUAGES:
            text=render_readme(self.config,self.prompts,lang)
            self.assertEqual(set(re.findall(r'<a id="([^"]+)"',text)),reference)
            for case in self.cases:
                if case['status']=='published': self.assertIn(page_path(case,lang),text)

    def test_local_navigation_is_inert_and_repository_badges_use_live_sources(self):
        for path, content in asset_outputs().items():
            root=ET.fromstring(content)
            self.assertTrue(root.tag.endswith('svg'))
            self.assertGreater(float(root.attrib['width']),0)
            self.assertNotIn('<script',content)
            self.assertNotIn('href=',content)
            self.assertNotIn('<image',content)
            self.assertEqual(path.read_text(),content)
        badges=repo_badges(self.config,'en')
        self.assertNotIn('passing',badges.lower())
        self.assertIn('https://awesome.re/badge.svg',badges)
        self.assertIn('https://img.shields.io/github/stars/RaphaelAI-OpenLab/awesome-gpt-image-2-6?style=social',badges)
        self.assertIn(repo_url(self.config)+'/actions/workflows/validate.yml/badge.svg?branch=main',badges)
        self.assertIn('https://img.shields.io/badge/License-MIT-lightgrey.svg',badges)
        self.assertNotIn('YouMind-OpenLab',badges)

    def test_canonical_repository_and_real_issue_templates(self):
        self.assertEqual(self.config['project']['repository_owner'],'RaphaelAI-OpenLab')
        for lang in LANGUAGES:
            text=render_readme(self.config,self.prompts,lang)
            self.assertNotIn('github.com/netlogs/',text)
            self.assertIn(repo_url(self.config)+'/issues/new?template=submit-case.yml',text)
            self.assertIn(repo_url(self.config)+'/issues/new?template=report-problem.yml',text)
        for template in ['submit-case.yml','report-problem.yml']:
            self.assertTrue((ROOT/'.github/ISSUE_TEMPLATE'/template).is_file())
        self.assertIn('CODE · MIT', messages('en'))


if __name__=='__main__': unittest.main()
