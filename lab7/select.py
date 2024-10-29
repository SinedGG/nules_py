import psycopg2
from decimal import Decimal
from datetime import date
from tabulate import tabulate

conn = psycopg2.connect(
    dbname="library",
    user="user",
    password="password",
    host="localhost"
)
cursor = conn.cursor()

def format_value(value):
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, date):
        return value.strftime("%Y-%m-%d")
    return value

# Запит 1: Відобразити всі книги, видані після 2001 року, відсортовані за назвою
cursor.execute('''
SELECT * FROM Books
WHERE publication_year > 2001
ORDER BY title;
''')
books = [list(map(format_value, row)) for row in cursor.fetchall()]
headers = ["ID", "Інвентарний номер", "Автор", "Назва", "Розділ", "Рік видання", "Сторінки", "Ціна", "Тип", "Кількість", "Макс дні видачі"]
print("Книги, видані після 2001 року (відсортовані за назвою):")
print(tabulate(books, headers=headers, tablefmt="grid"))

# Запит 2: Порахувати кількість книг кожного виду
cursor.execute('''
SELECT type, COUNT(*) AS count
FROM Books
GROUP BY type;
''')
book_counts = cursor.fetchall()
headers = ["Тип", "Кількість"]
print("\nКількість книг кожного виду:")
print(tabulate(book_counts, headers=headers, tablefmt="grid"))

# Запит 3: Відобразити всіх читачів, які брали посібники, відсортовані за прізвищем
cursor.execute('''
SELECT DISTINCT r.*
FROM Readers r
JOIN BookLoans bl ON r.card_number = bl.reader_card_number
JOIN Books b ON bl.book_inventory_number = b.inventory_number
WHERE b.type = 'посібник'
ORDER BY r.last_name;
''')
readers = [list(map(format_value, row)) for row in cursor.fetchall()]
headers = ["ID", "Номер картки", "Прізвище", "Ім'я", "Телефон", "Адреса", "Курс", "Група"]
print("\nЧитачі, які брали посібники:")
print(tabulate(readers, headers=headers, tablefmt="grid"))

# Запит 4: Відобразити всі книги у вказаному розділі
section = 'технічна'  # Змінити за потребою
cursor.execute('''
SELECT * FROM Books
WHERE section = %s;
''', (section,))
books_by_section = [list(map(format_value, row)) for row in cursor.fetchall()]
print(f"\nКниги розділу '{section}':")
print(tabulate(books_by_section, headers=headers, tablefmt="grid"))

# Запит 5: Порахувати кінцевий термін повернення для кожної виданої книги
cursor.execute('''
SELECT b.title, r.last_name, r.first_name, bl.loan_date,
       (bl.loan_date + b.max_borrow_days * INTERVAL '1 day') AS due_date
FROM BookLoans bl
JOIN Books b ON bl.book_inventory_number = b.inventory_number
JOIN Readers r ON bl.reader_card_number = r.card_number;
''')
loan_due_dates = [list(map(format_value, row)) for row in cursor.fetchall()]
headers = ["Назва книги", "Прізвище читача", "Ім'я читача", "Дата видачі", "Кінцевий термін"]
print("\nКінцевий термін повернення кожної виданої книги:")
print(tabulate(loan_due_dates, headers=headers, tablefmt="grid"))

# Запит 6: Порахувати кількість посібників, книг та періодичних видань у кожному розділі
cursor.execute('''
SELECT section, type, COUNT(*) AS count
FROM Books
GROUP BY section, type;
''')
section_counts = cursor.fetchall()
headers = ["Розділ", "Тип", "Кількість"]
print("\nКількість посібників, книг та періодичних видань у кожному розділі:")
print(tabulate(section_counts, headers=headers, tablefmt="grid"))

cursor.close()
conn.close()
