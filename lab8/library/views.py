from django.shortcuts import render
from .models import Book, Reader, BookLoan

def home(request):
    context = {
        'books': Book.objects.all(),
        'readers': Reader.objects.all(),
        'book_loans': BookLoan.objects.all(),
        'student_name': "Березовський Денис",
        'group': "ІПЗ-22010бск",
    }
    return render(request, 'library/home.html', context)
