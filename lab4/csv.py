import csv
import random
from faker import Faker
from datetime import datetime

fake = Faker('uk_UA')

total_records = 2000
male_percentage = 0.6
female_percentage = 0.4

male_count = int(total_records * male_percentage)
female_count = total_records - male_count

start_date = datetime(1938, 1, 1)
end_date = datetime(2008, 12, 31)

patronymics_male = ['Іванович', 'Олександрович', 'Васильович', 'Миколайович', 'Петрович']
patronymics_female = ['Іванівна', 'Олександрівна', 'Василівна', 'Миколаївна', 'Петренко']

def generate_record(gender):
    if gender == 'Чоловік':
        full_name = fake.name_male()
        patronymic = random.choice(patronymics_male)
    else:
        full_name = fake.name_female()
        patronymic = random.choice(patronymics_female)

    name_parts = full_name.split(' ', 1)
    surname, name = name_parts


    birth_date = fake.date_between(start_date=start_date, end_date=end_date)
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [surname, name, patronymic, gender, birth_date, position, city, address, phone, email]

data = []

for _ in range(male_count):
    data.append(generate_record('Чоловік'))

for _ in range(female_count):
    data.append(generate_record('Жінка'))

header = ['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email']

with open('employees.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print("Дані успішно збережено в employees.csv")
