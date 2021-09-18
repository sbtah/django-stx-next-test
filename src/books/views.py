
import requests
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm, SearchBook
from django.views.generic import View, FormView
import datetime

API_KEY = 'AIzaSyBd3UStCx_0imS5cZTOAh16TwoRJOaRNO8'


# Checks if query is valid.
def is_valid_query(param):
    return param != '' and param is not None


# Lists all books in database.
def book_list(request):

    books = Book.objects.all()

    # Getting data from form names.
    title = request.GET.get('title',)
    author = request.GET.get('author',)
    date_from = request.GET.get('date_from',)
    date_to = request.GET.get('date_to',)
    isnb = request.GET.get('isbn',)
    min_pages = request.GET.get('min-pages',)
    max_pages = request.GET.get('max-pages',)
    link = request.GET.get('link',)
    language = request.GET.get('language',)

    # This filter title.
    if is_valid_query(title):

        books = books.filter(title__icontains=title)

    # This filter author.
    elif is_valid_query(author):

        books = books.filter(author__icontains=author)

    # This filter for ISBN Number.
    if is_valid_query(isnb):

        books = books.filter(isbn_number=isnb)

    # This filter for minimum number of pages.
    if is_valid_query(min_pages):

        books = books.filter(number_of_pages__gte=min_pages)

    if is_valid_query(max_pages):

        books = books.filter(number_of_pages__lte=max_pages)

    # This filter for link to cover.
    if is_valid_query(link):

        books = books.filter(link_to_cover=link)

    # This filter for language.
    if is_valid_query(language):

        books = books.filter(language=language)

    # This filter a dates.
    if is_valid_query(date_from):

        books = books.filter(date_published__gte=date_from)

    if is_valid_query(date_to):

        books = books.filter(date_published__lte=date_to)

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
            messages.success(request, 'Your book was added.')
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
        messages.success(request, 'Book updated.')
        return redirect('/books')

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'books/book_update.html', context)


# Delete a book.
def book_delete(request, pk):

    book = Book.objects.get(pk=pk)
    book.delete()

    return redirect('books: book-list')


#  Dunno how to progress this further.
#  What I need is  a function that will parse through a google Books api,
#  and instanciate selected books as a models in db.


class GoogleBooks(FormView):

    model = Book
    form_class = SearchBook
    template_name = "books/api_list.html"
    success_url = reverse_lazy("books:book-search")

    def book_search(self, value):
        param = {"q": value}
        api_url = "https://www.googleapis.com/books/v1/volumes"
        response = requests.get(url=api_url, params=param)
        books = response.json()["items"]

        # for item in items:
        #     print(item["volumeInfo"]["title"])

        return books

    def add_book_to_library(self, items):
        for book in items:
            Book.objects.create(
                title=book['volumeInfo']['title'],
                author=str(book['volumeInfo']['authors'][:]),
                date_published=str(book['volumeInfo']['publishedDate']),
                isbn_number=book['volumeInfo']['industryIdentifiers'],
                number_of_pages=int(book['volumeInfo']['pageCount']),
                link_to_cover=book['volumeInfo']['canonicalVolumeLink'],
                language=book['volumeInfo']['language'],
            )

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            books = self.book_search(keyword)
            self.add_book_to_library(books)
            return HttpResponseRedirect(reverse_lazy('books:book-list'))

        return reverse_lazy("books:book-search")
