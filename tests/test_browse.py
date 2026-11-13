"""核对网站分类数量、多语言外链，以及保留的内部案例分类。"""
import copy
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from browse import gallery_url_for_language, read_browse, read_web_gallery, render_browse, validate_browse, validate_web_gallery
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

    def test_website_snapshot_matches_the_verified_tags_and_counts(self):
        errors = []
        validate_web_gallery(self.config, errors)
        self.assertEqual(errors, [])
        gallery = read_web_gallery()
        self.assertEqual(gallery['source_url'], 'https://raphael.app/gpt-image-2-6-prompts')
        self.assertEqual(gallery['verified_at'], '2026-11-13')
        self.assertEqual(gallery['total'], 130)
        self.assertEqual([(item['id'], item['count']) for item in gallery['categories']], [
            ('gif-animation', 79), ('brand-products', 7), ('characters-consistency', 20),
            ('posters-typography', 6), ('markup-edits', 10), ('infographics', 8),
            ('svg-design-assets', 3), ('interiors-architecture', 2),
        ])

    def test_each_language_has_website_tags_counts_and_localized_tracked_routes(self):
        prefixes = {
            'en': '', 'zh-CN': 'zh', 'zh-TW': 'zh-Hant', 'ja-JP': 'ja',
            'ko-KR': 'ko', 'th-TH': 'th', 'vi-VN': 'vi', 'hi-IN': 'hi',
            'es-ES': 'es', 'es-419': 'es', 'de-DE': 'de', 'fr-FR': 'fr',
            'it-IT': 'it', 'pt-BR': 'pt', 'pt-PT': 'pt', 'tr-TR': 'tr',
        }
        gallery = read_web_gallery()
        expected = [('all', 'All', '全部', gallery['total'])] + [
            (item['id'], item['label']['en'], item['label']['zh-CN'], item['count'])
            for item in gallery['categories']
        ]
        for language in LANGUAGES:
            with self.subTest(language=language):
                text = render_readme(self.config, self.prompts, language)
                navigation = text.split('<a id="categories"></a>', 1)[1].split('<a id="contents"></a>', 1)[0]
                self.assertNotIn('|', navigation)
                self.assertNotIn('<details', navigation)
                self.assertNotIn('#source-case-', navigation)
                links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', navigation)
                self.assertEqual(len(links), 9)
                prefix = '/' + prefixes[language] if prefixes[language] else ''
                for (label, url), (category_id, english, chinese, count) in zip(links, expected):
                    self.assertEqual(label, ui(english, chinese, language) + f' ({count})')
                    parts = urlsplit(url)
                    self.assertEqual(parts.scheme, 'https')
                    self.assertEqual(parts.netloc, 'raphael.app')
                    suffix = '' if category_id == 'all' else '/' + category_id
                    self.assertEqual(parts.path, prefix + '/gpt-image-2-6-prompts' + suffix)
                    query = parse_qs(parts.query)
                    self.assertEqual(query, {
                        **{key: [value] for key, value in self.config['tracking'].items()},
                        'utm_content': ['category_' + category_id], 'utm_term': [language],
                    })

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

    def test_invalid_website_snapshot_is_rejected(self):
        for mutation, expected in (
            ('negative-total', 'web-gallery.total'),
            ('boolean-total', 'web-gallery.total'),
            ('invalid-date', 'web-gallery.verified_at'),
            ('invalid-source', 'web-gallery.source_url'),
            ('duplicate-category', 'duplicate category ID'),
            ('unknown-category', 'expected a configured category ID'),
            ('missing-category', 'include every configured category'),
            ('missing-label', 'bilingual labels required'),
            ('negative-count', 'count: expected a non-negative integer'),
            ('boolean-count', 'count: expected a non-negative integer'),
        ):
            with self.subTest(mutation=mutation):
                gallery = copy.deepcopy(read_web_gallery())
                if mutation == 'negative-total':
                    gallery['total'] = -1
                elif mutation == 'boolean-total':
                    gallery['total'] = True
                elif mutation == 'invalid-date':
                    gallery['verified_at'] = '2026-02-30'
                elif mutation == 'invalid-source':
                    gallery['source_url'] = 'https://example.com/gallery'
                elif mutation == 'duplicate-category':
                    gallery['categories'].append(copy.deepcopy(gallery['categories'][0]))
                elif mutation == 'unknown-category':
                    gallery['categories'][0]['id'] = 'unknown'
                elif mutation == 'missing-category':
                    gallery['categories'].pop()
                elif mutation == 'missing-label':
                    del gallery['categories'][0]['label']['zh-CN']
                elif mutation == 'negative-count':
                    gallery['categories'][0]['count'] = -1
                elif mutation == 'boolean-count':
                    gallery['categories'][0]['count'] = True
                errors = []
                with patch('browse.read_web_gallery', return_value=gallery):
                    validate_web_gallery(self.config, errors)
                self.assertTrue(any(expected in error for error in errors), errors)

    def test_overlapping_website_categories_do_not_need_to_sum_to_total(self):
        gallery = copy.deepcopy(read_web_gallery())
        gallery['categories'][0]['count'] = gallery['total']
        errors = []
        with patch('browse.read_web_gallery', return_value=gallery):
            validate_web_gallery(self.config, errors)
        self.assertEqual(errors, [])

    def test_website_navigation_requires_nonempty_brand_destinations(self):
        for field in ('gallery', 'category'):
            for value in (None, '', 'http://raphael.app/gallery', 'https://example.com/gallery'):
                with self.subTest(field=field, value=value):
                    config = copy.deepcopy(self.config)
                    if field == 'gallery':
                        config['brand']['gallery_url'] = value
                        expected = 'brand.gallery_url'
                    else:
                        config['categories'][0]['website_url'] = value
                        expected = 'categories.' + config['categories'][0]['id'] + '.website_url'
                    errors = []
                    validate_web_gallery(config, errors)
                    self.assertTrue(any(expected in error for error in errors), errors)

    def test_localized_gallery_links_preserve_functional_parameters_and_replace_utm(self):
        url = 'https://raphael.app/gpt-image-2-6-prompts?view=cards&utm_source=old#tags'
        localized = gallery_url_for_language(url, 'zh-CN')
        self.assertEqual(localized, 'https://raphael.app/zh/gpt-image-2-6-prompts?view=cards&utm_source=old#tags')
        config = copy.deepcopy(self.config)
        config['brand']['gallery_url'] = url
        text = render_browse(config, 'zh-CN')
        first_url = re.search(r'\]\(([^)]+)\)', text).group(1)
        parts = urlsplit(first_url)
        self.assertEqual(parts.fragment, 'tags')
        query = parse_qs(parts.query)
        self.assertEqual(query['view'], ['cards'])
        self.assertEqual(query['utm_source'], [config['tracking']['utm_source']])
        self.assertEqual(query['utm_term'], ['zh-CN'])

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
