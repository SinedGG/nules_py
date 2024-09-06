from text_translation.googletrans_module import TransLate, LangDetect, CodeLang, LanguageList

print("=== Демонстрація TransLate ===")
translated_text = TransLate("Hello, world!", "en", "uk")
print(f"Переклад з англійської на українську: {translated_text}")

# Демонстрація роботи функції LangDetect
print("\n=== Демонстрація LangDetect ===")
detected_lang = LangDetect("Bonjour tout le monde", "lang")
print(f"Визначена мова: {detected_lang}")

detected_confidence = LangDetect("Bonjour tout le monde", "confidence")
print(f"Коефіцієнт довіри: {detected_confidence}")

# Демонстрація роботи функції CodeLang
print("\n=== Демонстрація CodeLang ===")
lang_code = CodeLang("ukrainian")
print(f"Код мови 'ukrainian': {lang_code}")

lang_name = CodeLang("uk")
print(f"Назва мови з кодом 'uk': {lang_name}")

# Демонстрація роботи функції LanguageList
print("\n=== Демонстрація LanguageList ===")
result = LanguageList("screen", "Добрий день")
print(result)