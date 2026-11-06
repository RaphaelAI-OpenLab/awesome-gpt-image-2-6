"""Explicit locale routes and source-keyed UI translations, standard library only."""
from functools import lru_cache
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
LANGUAGE_NAMES = {
    'en': 'English', 'zh-CN': '简体中文', 'zh-TW': '繁體中文',
    'ja-JP': '日本語', 'ko-KR': '한국어', 'th-TH': 'ไทย',
    'vi-VN': 'Tiếng Việt', 'hi-IN': 'हिन्दी', 'es-ES': 'Español',
    'es-419': 'Español (Latinoamérica)', 'de-DE': 'Deutsch', 'fr-FR': 'Français',
    'it-IT': 'Italiano', 'pt-BR': 'Português (Brasil)', 'pt-PT': 'Português', 'tr-TR': 'Türkçe',
}
LANGUAGES = tuple(LANGUAGE_NAMES)
DETAIL_LANGUAGES = ('en', 'zh-CN')


def filename(language):
    if language not in LANGUAGE_NAMES:
        raise ValueError(f'Unsupported locale: {language}')
    return 'README.md' if language == 'en' else f'README.{language}.md'


def detail_language(language):
    if language not in LANGUAGE_NAMES:
        raise ValueError(f'Unsupported locale: {language}')
    return language if language in DETAIL_LANGUAGES else 'en'


@lru_cache(maxsize=None)
def messages(language):
    return json.loads((ROOT / 'content' / 'locales' / f'{language}.json').read_text(encoding='utf-8'))['messages']


def ui(english, chinese=None, language='en'):
    """UI copy must be translated; never silently publish English interface text."""
    if language == 'en':
        return english
    if language == 'zh-CN' and chinese is not None:
        return chinese
    return messages(language)[english]


def translated_source(english, language):
    """Category/status labels may have translations; case prose stays at source."""
    if language == 'en':
        return english
    return messages(language).get(english, english)
