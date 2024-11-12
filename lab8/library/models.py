from django.db import models

class Book(models.Model):
    inventory_number = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    section = models.CharField(max_length=20, choices=[('технічна', 'технічна'), ('художня', 'художня'), ('економічна', 'економічна')])
    publication_year = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=[('посібник', 'посібник'), ('книга', 'книга'), ('періодичне видання', 'періодичне видання')])
    copies = models.PositiveIntegerField(default=1)
    max_borrow_days = models.PositiveIntegerField(default=30)

    class Meta:
        db_table = 'library_book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class Reader(models.Model):
    card_number = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    course = models.PositiveIntegerField()
    group_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'library_reader'
        verbose_name = 'Reader'
        verbose_name_plural = 'Readers'

class BookLoan(models.Model):
    loan_date = models.DateField()
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'library_bookloan'
        verbose_name = 'Book Loan'
        verbose_name_plural = 'Book Loans'

