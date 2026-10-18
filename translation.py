import locale
import json
import glob
import os


class Translation:
    _translations_path = os.path.join(os.path.dirname(__file__), 'translations')
    _translations = []
    _default_translations = []
    _legacy_language_codes = {
        'se': 'sv',
    }

    @staticmethod
    def _language_code(locale_name):
        if not locale_name:
            return None

        language = str(locale_name).strip().split('@', 1)[0].split('.', 1)[0]
        language = language.replace('-', '_').split('_', 1)[0].lower()
        if language in ('', 'c', 'posix'):
            return None

        return language

    @staticmethod
    def _system_language_codes():
        system_locale = None
        for variable in ('LC_ALL', 'LC_MESSAGES', 'LANG'):
            value = os.environ.get(variable)
            if value:
                system_locale = value
                break

        if system_locale is None:
            try:
                system_locale = locale.getlocale(locale.LC_MESSAGES)[0]
            except (AttributeError, locale.Error, TypeError, ValueError):
                system_locale = None

        # A C/POSIX message locale explicitly disables localized messages.
        if system_locale:
            base_locale = system_locale.strip().split('@', 1)[0].split('.', 1)[0].lower()
            if base_locale in ('c', 'posix'):
                return []

        language_codes = []
        language_preferences = os.environ.get('LANGUAGE', '')
        for preference in language_preferences.split(':'):
            code = Translation._language_code(preference)
            if code and code not in language_codes:
                language_codes.append(code)

        code = Translation._language_code(system_locale)
        if code and code not in language_codes:
            language_codes.append(code)

        return language_codes

    @staticmethod
    def select_language(lang_code="auto"):
        use_system_language = not lang_code or str(lang_code).strip().lower() == 'auto'
        if use_system_language:
            language_codes = Translation._system_language_codes()
        else:
            code = Translation._language_code(lang_code)
            language_codes = [code] if code else []

        available_languages = set(Translation.available_languages())
        Translation.lang_code = 'en'
        for code in language_codes:
            if code in available_languages:
                Translation.lang_code = code
                break

            # Keep existing user configs that selected Swedish as "se" working.
            if not use_system_language and code in Translation._legacy_language_codes:
                legacy_code = Translation._legacy_language_codes[code]
                if legacy_code in available_languages:
                    Translation.lang_code = legacy_code
                    break

        Translation._load_lang(Translation.lang_code)

    @staticmethod
    def _load_lang(lang_code):
        file_path = Translation._translations_path + '/' + lang_code + ".json"
        if os.path.isfile(file_path):
            with open(file_path) as json_file:
                Translation._translations = json.load(json_file)

        file_path_en = Translation._translations_path + "/en.json"
        if os.path.isfile(file_path_en):
            with open(file_path_en) as json_file:
                Translation._default_translations = json.load(json_file)

    @staticmethod
    def available_languages():
        return [os.path.splitext(os.path.basename(x))[0] for x in glob.glob(Translation._translations_path + '/*.json')]

    @staticmethod
    def t(translation):
        if not Translation._translations:
            Translation.select_language()
        if translation in Translation._translations:
            return Translation._translations[translation]
        elif translation in Translation._default_translations:
            return Translation._default_translations[translation]
