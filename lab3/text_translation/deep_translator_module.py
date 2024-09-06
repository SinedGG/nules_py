from deep_translator import GoogleTranslator


def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translated = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Error: {e}"


def LangDetect(text: str, set: str = "all") -> str:
    from langdetect import detect, DetectorFactory
    DetectorFactory.seed = 0
    try:
        lang = detect(text)
        confidence = 1.0
        if set == "lang":
            return lang
        elif set == "confidence":
            return str(confidence)
        else:
            return f"{lang}, {confidence}"
    except Exception as e:
        return f"Error: {e}"


def CodeLang(lang: str) -> str:
    try:
        translator = GoogleTranslator()
        lang_map = translator.get_supported_languages(as_dict=True)

        # Якщо введено назву мови
        if lang.lower() in lang_map.values():
            for code, name in lang_map.items():
                if name.lower() == lang.lower():
                    return code
        # Якщо введено код мови
        elif lang.lower() in lang_map:
            return lang_map[lang.lower()]
        else:
            return "Error: Language not found"
    except Exception as e:
        return f"Error: {e}"


def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        translator = GoogleTranslator()
        lang_map = translator.get_supported_languages(as_dict=True)

        table = "N Language ISO-639 code Text\n" + "-" * 50 + "\n"
        result = []
        for i, (code, name) in enumerate(lang_map.items(), start=1):
            translated_text = GoogleTranslator(source='auto', target=code).translate(text) if text else ""
            line = f"{i} {name} {code} {translated_text}".strip()
            result.append(line)

        table += "\n".join(result)

        if out == "screen":
            print(table)
        elif out == "file":
            with open("language_list_deep.txt", "w", encoding="utf-8") as f:
                f.write(table)

        return "Ok"
    except Exception as e:
        return f"Error: {e}"
