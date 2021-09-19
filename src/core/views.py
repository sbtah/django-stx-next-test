from django.shortcuts import render
from books.models import Book


# This function will greet visitors with
def home_view(request):

    all_books = Book.objects.all().count()

    return render(request, 'core/home.html', {
        'all_books': all_books,
    })
