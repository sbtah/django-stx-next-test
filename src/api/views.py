from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BookSerializer
from books.models import Book


# Api Stuff.
class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
