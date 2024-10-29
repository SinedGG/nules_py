import psycopg2
from faker import Faker
from random import choice, randint

fake = Faker('uk_UA')

conn = psycopg2.connect(
    dbname="library",
    user="user",
    password="password",
    host="localhost"
)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS BookLoans CASCADE;")
cursor.execute("DROP TABLE IF EXISTS Readers CASCADE;")
cursor.execute("DROP TABLE IF EXISTS Books CASCADE;")

cursor.execute('''
CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    inventory_number VARCHAR(50) NOT NULL UNIQUE,
    author VARCHAR(100) NOT NULL,
    title VARCHAR(200) NOT NULL,
    section VARCHAR(20) CHECK (section IN ('технічна', 'художня', 'економічна')),
    publication_year INTEGER CHECK (publication_year > 0),
    pages INTEGER CHECK (pages > 0),
    price NUMERIC CHECK (price >= 0),
    type VARCHAR(20) CHECK (type IN ('посібник', 'книга', 'періодичне видання')),
    copies INTEGER DEFAULT 1 CHECK (copies >= 0),
    max_borrow_days INTEGER DEFAULT 30 CHECK (max_borrow_days > 0)
);
''')

cursor.execute('''
CREATE TABLE Readers (
    id SERIAL PRIMARY KEY,
    card_number VARCHAR(50) NOT NULL UNIQUE,
    last_name VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    course INTEGER CHECK (course BETWEEN 1 AND 4),
    group_name VARCHAR(50)
);
''')

cursor.execute('''
CREATE TABLE BookLoans (
    id SERIAL PRIMARY KEY,
    loan_date DATE NOT NULL,
    reader_card_number VARCHAR(50) NOT NULL REFERENCES Readers(card_number) ON DELETE CASCADE,
    book_inventory_number VARCHAR(50) NOT NULL REFERENCES Books(inventory_number) ON DELETE CASCADE
);
''')

books_data = [
    (
        f"INV{str(fake.unique.random_int(min=100, max=999)).zfill(3)}",
        fake.name(),
        fake.catch_phrase(),
        choice(['технічна', 'художня', 'економічна']),
        fake.year(),
        randint(100, 800),
        round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
        choice(['посібник', 'книга', 'періодичне видання']),
        randint(1, 5),
        randint(15, 90)
    ) for _ in range(14)
]

readers_data = [
    (
        f"CN{str(fake.unique.random_int(min=100, max=999)).zfill(3)}",
        fake.last_name(),
        fake.first_name(),
        fake.phone_number(),
        fake.address(),
        randint(1, 4),
        f"Група {randint(1, 4)}"
    ) for _ in range(9)
]

cursor.executemany('''
INSERT INTO Books (inventory_number, author, title, section, publication_year, pages, price, type, copies, max_borrow_days)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
''', books_data)

cursor.executemany('''
INSERT INTO Readers (card_number, last_name, first_name, phone, address, course, group_name)
VALUES (%s, %s, %s, %s, %s, %s, %s);
''', readers_data)

book_loans_data = [
    (
        fake.date_this_year(),
        choice([reader[0] for reader in readers_data]),
        choice([book[0] for book in books_data])
    ) for _ in range(11)
]

cursor.executemany('''
INSERT INTO BookLoans (loan_date, reader_card_number, book_inventory_number)
VALUES (%s, %s, %s);
''', book_loans_data)

conn.commit()
cursor.close()
conn.close()
print("Successfully.")
