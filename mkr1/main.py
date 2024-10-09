import os
import json
from utils import calculate_bonus, get_translations, is_valid_language

# Шлях до файлу з даними
data_file = "MyData.json"


def read_data():
    if os.path.exists(data_file):
        with open(data_file, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                print("Некоректні дані у файлі.")
    return None


def write_data(salary, experience, language):
    data = {
        "salary": salary,
        "experience": experience,
        "language": language
    }
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Дані збережено в файл {data_file}")


def main():
    data = read_data()

    if not data:
        # Якщо дані не прочитані або некоректні
        salary = float(input("Введіть розмір зарплати (грн): "))
        experience = int(input("Введіть стаж (кількість років): "))
        language = input("Введіть мову інтерфейсу (uk/інша): ")

        # Якщо мова некоректна, використовуємо українську за замовчуванням
        if not is_valid_language(language):
            print("Мову введено некоректно. Використовується українська.")
            language = "uk"

        write_data(salary, experience, language)
        return

    # Успішне прочитання даних
    language = data.get("language", "uk")
    salary = data["salary"]
    experience = data["experience"]

    # Якщо мова не українська і коректна, перекладаємо інтерфейс
    if language != "uk" and is_valid_language(language):
        translations = get_translations(language)
    else:
        translations = {
            "language": "Українська",
            "salary": "Зарплата",
            "experience": "Стаж",
            "bonus_percent": "Надбавка (%)",
            "bonus_amount": "Надбавка (грн)",
            "total": "Всього"
        }

    bonus_percent, bonus_amount, total = calculate_bonus(salary, experience)

    # Вивести результат
    print(f"{translations['language']}:")
    print(f"{translations['salary']}: {salary} грн.")
    print(f"{translations['experience']}: {experience} років.")
    print(f"{translations['bonus_percent']}: {bonus_percent}%")
    print(f"{translations['bonus_amount']}: {bonus_amount} грн")
    print(f"{translations['total']}: {total} грн.")


if __name__ == "__main__":
    main()
