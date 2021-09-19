from books.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book

        fields = [
            'title',
            'author',
            'date_published',
            'isbn_number',
            'number_of_pages',
            'link_to_cover',
            'language'
        ]
