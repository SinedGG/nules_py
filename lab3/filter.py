import json
import os
import re
from text_translation.deep_translator_module import TransLate, LangDetect


def read_config(config_path):
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("Error: Config file not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Config file is not valid JSON.")
        return None


def read_text_file(text_file, max_characters, max_words, max_sentences):
    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            content = file.read()

        content = content[:max_characters]
        words = re.findall(r'\b\w+\b', content)  # Знаходить слова
        sentences = re.split(r'[.!?]', content)  # Розбиває на речення

        if len(words) > max_words:
            content = ' '.join(words[:max_words])
        if len(sentences) > max_sentences:
            content = '. '.join(sentences[:max_sentences])

        return content
    except FileNotFoundError:
        print("Error: Text file not found.")
        return None
    except Exception as e:
        print(f"Error reading text file: {e}")
        return None


def get_text_stats(text):
    characters = len(text)
    words = len(re.findall(r'\b\w+\b', text))
    sentences = len(re.split(r'[.!?]', text)) - 1
    return characters, words, sentences


def main():
    config_path = "config.json"
    config = read_config(config_path)

    if not config:
        return

    text_file = config.get("text_file")
    target_language = config.get("target_language")
    output = config.get("output")
    max_characters = config.get("max_characters", 600)
    max_words = config.get("max_words", 100)
    max_sentences = config.get("max_sentences", 10)

    text = read_text_file(text_file, max_characters, max_words, max_sentences)

    if not text:
        return

    characters, words, sentences = get_text_stats(text)

    print(f"=== Інформація про файл ===")
    print(f"Назва файлу: {text_file}")
    print(f"Кількість символів: {characters}")
    print(f"Кількість слів: {words}")
    print(f"Кількість речень: {sentences}")

    lang = LangDetect(text, set="lang")
    print(f"Мова тексту: {lang}")

    translated_text = TransLate(text, scr=lang, dest=target_language)

    if "Error" in translated_text:
        print(f"Error during translation: {translated_text}")
        return

    if output == "screen":
        print(f"\n=== Перекладено на мову: {target_language} ===")
        print(translated_text)
    elif output == "file":
        output_file = f"{os.path.splitext(text_file)[0]}_{target_language}.txt"
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(translated_text)
            print("Ok")
        except Exception as e:
            print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()
