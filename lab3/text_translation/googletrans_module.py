from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"{detection.lang}, {detection.confidence}"
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str) -> str:
    if lang.lower() in LANGUAGES.values():
        for code, name in LANGUAGES.items():
            if name.lower() == lang.lower():
                return code
    elif lang.lower() in LANGUAGES:
        return LANGUAGES[lang.lower()]
    else:
        return "Error: Language not found"

def LanguageList(out: str = "screen", text: str = None) -> str:
    table = "N Language ISO-639 code Text\n" + "-" * 50 + "\n"
    result = []
    try:
        for i, (code, name) in enumerate(LANGUAGES.items(), start=1):
            translated_text = translator.translate(text, dest=code).text if text else ""
            line = f"{i} {name} {code} {translated_text}".strip()
            result.append(line)

        table += "\n".join(result)

        if out == "screen":
            print(table)
        elif out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as f:
                f.write(table)

        return "Ok"
    except Exception as e:
        return f"Error: {e}"
