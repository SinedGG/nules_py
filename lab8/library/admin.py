from django.contrib import admin
from .models import Book, Reader, BookLoan

admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(BookLoan)
