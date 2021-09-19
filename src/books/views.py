
import requests
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm, SearchBook
from django.views.generic import View, FormView
import datetime


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
#  What I need is  a function or view that will parse through a google Books api,
#  and instanciate selected books as a models in db.
class GoogleBooks(FormView):

    model = Book
    form_class = SearchBook
    template_name = "books/google_search.html"
    success_url = reverse_lazy("books:book-search")

    def book_search(self, value):
        param = {"q": value}
        api_url = "https://www.googleapis.com/books/v1/volumes"
        response = requests.get(url=api_url, params=param)
        books = response.json()["items"]

        # for item in books:
        #     print(item['volumeInfo']['publishedDate'][:4])

        return books

    def add_book_to_library(self, items):

        try:
            # just in case the server doesn't return valid JSON
            for result in items:
                if "volumeInfo" not in result:  # invalid entry - missing volumeInfo
                    continue

                result_dict = {}  # a dictionary to store our discovered fields
                # all the data we're interested is in volumeInfo.
                result = result["volumeInfo"]

                result_dict["title"] = result.get("title", None)
                result_dict["author"] = result.get("authors", None)
                result_dict["published_date"] = result.get(
                    "publishedDate", None)
                result_dict["isbn"] = result.get("industryIdentifiers", None)
                result_dict["pages"] = result.get("pageCount", None)
                result_dict["image_link"] = result.get(
                    "imageLinks", {}).get("thumbnail", None)
                result_dict["language"] = result.get("language", None)

                Book.objects.create(
                    title=str(result_dict["title"]),
                    author=str(result_dict["author"]),
                    date_published=str(result_dict["published_date"]),
                    isbn_number=str(result_dict["isbn"]),
                    number_of_pages=str(result_dict["pages"]),
                    link_to_cover=str(result_dict["image_link"]),
                    language=str(result_dict["language"]),
                )
        # There is an error here, in some value or maybe I'm bad at unpacking this.... :(
        except ValueError:
            print("error")

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            books = self.book_search(keyword)
            self.add_book_to_library(books)
            return HttpResponseRedirect(reverse_lazy('books:book-list'))

        return reverse_lazy("books:book-search")
