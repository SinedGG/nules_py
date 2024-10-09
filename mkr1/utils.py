from googletrans import Translator, LANGUAGES


def calculate_bonus(salary, experience):
    if experience < 0 or experience > 70:
        raise ValueError("Некоректний стаж (0 <= стаж <= 70).")

    if experience < 2:
        bonus_percent = 0
    elif 2 <= experience <= 5:
        bonus_percent = 2
    elif 5 < experience <= 10:
        bonus_percent = 5
    else:
        bonus_percent = 10

    bonus_amount = salary * bonus_percent / 100
    total = salary + bonus_amount
    return bonus_percent, bonus_amount, total


def get_translations(language):
    translator = Translator()

    texts_to_translate = {
        "language": "Мова",
        "salary": "Зарплата",
        "experience": "Стаж",
        "bonus_percent": "Надбавка (%)",
        "bonus_amount": "Надбавка (грн)",
        "total": "Всього"
    }

    translations = {}
    for key, value in texts_to_translate.items():
        translated = translator.translate(value, dest=language).text
        translations[key] = translated

    return translations


def is_valid_language(language):
    return language in LANGUAGES
