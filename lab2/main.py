from google.cloud import translate_v2 as translate
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'api.json'
translate_client = translate.Client()

def TransLate(text, lang):
    try:
        result = translate_client.translate(text, target_language=lang)
        return result['translatedText']
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text):
    try:
        result = translate_client.detect_language(text)
        language = result['language']
        confidence = result['confidence']
        return language, confidence
    except Exception as e:
        return f"Error: {str(e)}", 0

def CodeLang(lang):
    try:
        languages = translate_client.get_languages()
        lang_dict = {lang['language']: lang['name'].lower() for lang in languages}

        if lang in lang_dict:
            return lang_dict[lang].capitalize()

        for code, name in lang_dict.items():
            if name == lang.lower():
                return code

        return None
    except Exception as e:
        return f"Error: {str(e)}"

txt = "Доброго дня. Як справи?"
lang = "en"
print(txt)
print(LangDetect(txt))
print(TransLate(txt, lang))
print(CodeLang(lang))

