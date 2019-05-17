import locale
import json
import glob
import os


class Translation:
    translations_path = os.path.join(os.path.dirname(__file__), 'translations')
    translations = []

    @staticmethod
    def select_language(lang_code=""):
        if not lang_code:
            default_locale = locale.getdefaultlocale()[0]
            lang = default_locale.split("_")
            lang_code = lang[0] if len(lang) else "en"

        if lang_code in Translation.available_languages():
            Translation.lang_code = lang_code
        else:
            Translation.lang_code = "en"

        Translation.load_lang(Translation.lang_code)

    @staticmethod
    def load_lang(lang_code):
        with open(Translation.translations_path + '/' + lang_code + ".json") as json_file:
            Translation.translations = json.load(json_file)

    @staticmethod
    def available_languages():
        return [os.path.splitext(os.path.basename(x))[0] for x in glob.glob(Translation.translations_path + '/*.json')]

    @staticmethod
    def t(translation):
        if not Translation.translations:
            Translation.select_language()
        if translation in Translation.translations:
            return Translation.translations[translation]
