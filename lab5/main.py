import re
import string

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            sentences = re.split(r'(?<=[.!?]) +', text)
            first_sentence = sentences[0] if sentences else ""
            print("Перше речення:", first_sentence)
            return first_sentence
    except FileNotFoundError:
        print("Файл не знайдено.")
        return ""
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return ""

def clean_word(word):
    return word.strip(string.punctuation).lower()

def sort_words(text):
    words = re.findall(r'\b\w+\b', text)
    words = [clean_word(w) for w in words if w]
    ukrainian_words = [w for w in words if re.match(r'[А-Яа-я]', w)]
    english_words = [w for w in words if re.match(r'[A-Za-z]', w)]
    ukrainian_words.sort()
    english_words.sort()
    sorted_words = ukrainian_words + english_words
    return sorted_words

file_path = 'text_file.txt'

first_sentence = read_first_sentence(file_path)
if first_sentence:
    sorted_words = sort_words(first_sentence)
    print("Відсортовані слова:", sorted_words)
    print("Кількість слів:", len(sorted_words))
