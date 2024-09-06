import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os


def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


csv_file = 'employees.csv'
if not os.path.exists(csv_file):
    print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV")
else:
    try:
        df = pd.read_csv(csv_file)

        required_columns = ['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Стать']
        for col in required_columns:
            if col not in df.columns:
                print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV")
                break
        else:
            df['Дата народження'] = pd.to_datetime(df['Дата народження'], errors='coerce')
            df = df.dropna(subset=['Дата народження'])

            df['Вік'] = df['Дата народження'].apply(calculate_age)

            gender_counts = df['Стать'].value_counts()
            print("Кількість співробітників за статтю:")
            print(gender_counts)

            # Побудова діаграми за статтю
            plt.figure(figsize=(10, 6))
            gender_counts.plot(kind='bar', color=['blue', 'pink'])
            plt.title('Кількість співробітників за статтю')
            plt.xlabel('Стать')
            plt.ylabel('Кількість')
            plt.xticks(rotation=0)
            plt.tight_layout()
            plt.show()

            age_categories = pd.cut(df['Вік'], bins=[-1, 18, 45, 70, float('inf')],
                                    labels=['Younger_18', '18-45', '45-70', 'Older_70'])
            age_category_counts = age_categories.value_counts()
            print("\nКількість співробітників за віковими категоріями:")
            print(age_category_counts)

            plt.figure(figsize=(10, 6))
            age_category_counts.plot(kind='bar', color='skyblue')
            plt.title('Кількість співробітників за віковими категоріями')
            plt.xlabel('Вікова категорія')
            plt.ylabel('Кількість')
            plt.xticks(rotation=0)
            plt.tight_layout()
            plt.show()

            gender_age_category_counts = df.groupby([age_categories, 'Стать'], observed=False).size().unstack(
                fill_value=0)
            print("\nКількість співробітників за статтю в кожній віковій категорії:")
            print(gender_age_category_counts)

            for category in gender_age_category_counts.index:
                plt.figure(figsize=(10, 6))
                gender_age_category_counts.loc[category].plot(kind='bar', color=['blue', 'pink'])
                plt.title(f'Кількість співробітників за статтю в віковій категорії {category}')
                plt.xlabel('Стать')
                plt.ylabel('Кількість')
                plt.xticks(rotation=0)
                plt.tight_layout()
                plt.show()

            print("Ок")
    except Exception as e:
        print("Повідомлення про неможливість обробки CSV файлу")
