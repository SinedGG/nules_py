import pandas as pd
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

        required_columns = ['Прізвище', 'Ім’я', 'По батькові', 'Дата народження']
        for col in required_columns:
            if col not in df.columns:
                print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV")
                break
        else:
            df['Дата народження'] = pd.to_datetime(df['Дата народження'], errors='coerce')
            df = df.dropna(subset=['Дата народження'])

            df['Вік'] = df['Дата народження'].apply(calculate_age)

            df_all = df
            df_younger_18 = df[df['Вік'] < 18]
            df_18_45 = df[(df['Вік'] >= 18) & (df['Вік'] <= 45)]
            df_45_70 = df[(df['Вік'] > 45) & (df['Вік'] <= 70)]
            df_older_70 = df[df['Вік'] > 70]

            with pd.ExcelWriter('employees.xlsx', engine='openpyxl') as writer:
                df_all.to_excel(writer, sheet_name='all', index=False)
                df_younger_18.to_excel(writer, sheet_name='younger_18', index=False)
                df_18_45.to_excel(writer, sheet_name='18-45', index=False)
                df_45_70.to_excel(writer, sheet_name='45-70', index=False)
                df_older_70.to_excel(writer, sheet_name='older_70', index=False)

            print("Ok")
    except Exception as e:
        print("Повідомлення про неможливість створення XLSX файлу")
