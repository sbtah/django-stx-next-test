from django.shortcuts import render
from books.models import Book


def home_view(request):

    all_books = Book.objects.all().count()

    return render(request, 'core/home.html', {
        'all_books': all_books,
    })
