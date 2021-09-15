from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm


# Lists all books in database.
def book_list(request):

    books = Book.objects.all()

    return render(request, 'books/book_list.html', {
        'books': books,
    })


# Creates a book.
def book_create(request):

    submitted = False

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/?submitted=True')
    else:
        form = BookForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'books/book_create.html', context)


# Updates a book.
def book_update(request, pk):

    post = Book.objects.get(pk=pk)

    form = BookForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()

        return redirect('/books')

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'books/book_update.html', context)
