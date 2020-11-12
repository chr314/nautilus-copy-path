import locale
import json
import glob
import os


class Translation:
    _translations_path = os.path.join(os.path.dirname(__file__), 'translations')
    _translations = []

    @staticmethod
    def select_language(lang_code=""):
        if not lang_code:
            default_locale = locale.getdefaultlocale()[0]
            try:
                lang = default_locale.split("_")
                lang_code = lang[0] if len(lang) else "en"
            except AttributeError:
                lang_code = "en"
        if lang_code in Translation.available_languages():
            Translation.lang_code = lang_code
        else:
            Translation.lang_code = "en"

        Translation._load_lang(Translation.lang_code)

    @staticmethod
    def _load_lang(lang_code):
        file_path = Translation._translations_path + '/' + lang_code + ".json"
        if os.path.isfile(file_path):
            with open(file_path) as json_file:
                Translation._translations = json.load(json_file)

    @staticmethod
    def available_languages():
        return [os.path.splitext(os.path.basename(x))[0] for x in glob.glob(Translation._translations_path + '/*.json')]

    @staticmethod
    def t(translation):
        if not Translation._translations:
            Translation.select_language()
        if translation in Translation._translations:
            return Translation._translations[translation]
