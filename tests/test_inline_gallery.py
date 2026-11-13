"""核对 README 完整展示、原文对应关系与缺失提示词边界。"""
import copy
import re
import sys
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from common import ROOT, code_block, load_data, read_json
from i18n import LANGUAGES, ui
from source_cases import read_cases, render_inline_case, render_original_prompt, video_preview_path, visible
from validate import validate_source_cases


class InlineGalleryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config, _ = load_data()
        cls.cases = visible(read_cases())

    def test_all_public_prompts_have_text_and_ailingqu_matches_retained_originals(self):
        by_id = {item['id']: item for item in self.cases}
        for item in self.cases:
            if item['prompt']['status'] == 'source-only':
                self.assertTrue(item['prompt'].get('entries'), item['id'])
        for original in read_json('docs/ailingqu-2037/verified-prompts.json'):
            entries = by_id[original['case_id']]['prompt']['entries']
            self.assertIn(original['complete_submitted_prompt_as_documented'], [entry['text'] for entry in entries])

    def test_all_languages_show_each_output_prompt_and_bottom_credit(self):
        for language in LANGUAGES:
            for item in self.cases:
                with self.subTest(language=language, case=item['id']):
                    card = render_inline_case(item, language, 1, self.config)
                    for media in item['media']:
                        if not media['path']:
                            continue
                        if media.get('role') == 'reference':
                            self.assertNotIn('src="' + media['path'] + '"', card)
                        else:
                            path = video_preview_path(media) if media['kind'] == 'video' else media['path']
                            self.assertIn('src="' + path + '"', card)
                            self.assertTrue((ROOT / path).is_file())
                    for entry in item['prompt'].get('entries', []):
                        self.assertIn(code_block(entry['text']), card)
                    self.assertIn(item['source']['author'], card)
                    self.assertGreater(card.rfind(item['source']['author']), card.rfind('```'))
                    footer = card.rstrip().splitlines()[-1]
                    match = re.fullmatch(r'\*\*\[👉 (.+)\]\(([^)]+)\)\*\*', footer)
                    self.assertIsNotNone(match)
                    self.assertEqual(match.group(1), ui('Try now →', '立即尝试 →', language))
                    target = urlsplit(match.group(2))
                    self.assertEqual((target.scheme, target.netloc, target.path),
                                     ('https', 'raphael.app', '/gpt-image-2-6-prompts'))
                    query = parse_qs(target.query)
                    self.assertEqual(query['utm_content'], ['case_gallery_' + item['id']])
                    self.assertEqual(query['utm_term'], [language])
                    self.assertNotIn('id', query)

    def test_featured_cases_also_end_with_the_gallery_button(self):
        item = self.cases[0]
        for language in LANGUAGES:
            with self.subTest(language=language):
                regular = render_inline_case(item, language, 1, self.config)
                featured = render_inline_case(item, language, 1, self.config, featured=True)
                self.assertEqual(featured.rstrip().splitlines()[-1], regular.rstrip().splitlines()[-1])
                self.assertIn('**[👉 ', featured.rstrip().splitlines()[-1])

    def test_missing_prompts_never_render_code_and_unknowns_are_not_called_private(self):
        item = copy.deepcopy(self.cases[0])
        for status in ('not-public', 'unverified'):
            item['prompt'] = {'status': status, 'url': None}
            for language in ('en', 'zh-CN'):
                text = render_original_prompt(item, language)
                self.assertNotIn('```', text)
                if status == 'unverified':
                    self.assertNotIn('not public', text)
                    self.assertNotIn('未公开', text)

    def test_copied_text_requires_public_status_and_real_source(self):
        original = next(item for item in self.cases if item['prompt'].get('entries'))
        for mutation in ('private', 'empty', 'missing-source'):
            item = copy.deepcopy(original)
            if mutation == 'private':
                item['prompt'].update(status='not-public', url=None)
            elif mutation == 'empty':
                item['prompt']['entries'][0]['text'] = ' '
            else:
                item['prompt']['entries'][0]['url'] = 'not-a-source'
            errors = []
            validate_source_cases(self.config, [item], [], errors)
            self.assertTrue(any('.prompt.entries' in error for error in errors), mutation)

    def test_prompt_text_file_matches_original_and_has_safe_local_links(self):
        item = copy.deepcopy(self.cases[0])
        item['media'] = []
        item.pop('access', None)
        entry = {'title': {'en': 'Original prompt', 'zh-CN': '原始提示词'},
                 'text': 'Make this cat wave.\nKeep the camera still.',
                 'url': item['source']['url'], 'path': f"cases/{item['id']}/prompt.txt"}
        item['prompt'] = {'status': 'source-only', 'url': item['source']['url'], 'entries': [entry]}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / entry['path']
            target.parent.mkdir(parents=True)
            target.write_text(entry['text'] + '\n', encoding='utf-8')
            with patch('validate.ROOT', root):
                errors = []
                validate_source_cases(self.config, [item], [], errors)
                self.assertEqual(errors, [])
                target.write_text('Rewritten prompt\n', encoding='utf-8')
                validate_source_cases(self.config, [item], [], errors)
                self.assertTrue(any('exactly match' in error for error in errors))
            for language in ('en', 'zh-CN'):
                self.assertIn('](' + entry['path'] + ')', render_original_prompt(item, language))
                self.assertIn('](../../' + entry['path'] + ')', render_original_prompt(item, language, prefix='../../'))


if __name__ == '__main__':
    unittest.main()
