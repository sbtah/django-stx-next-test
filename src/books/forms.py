from .models import Book
from django import forms


class BookForm(forms.ModelForm):

    class Meta:

        model = Book

        fields = ('title', 'author', 'date_published', 'isbn_number',
                  'number_of_pages', 'link_to_cover', 'language')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'author': forms.TextInput(attrs={'class': 'form-control', }),
            'date_published': forms.DateInput(attrs={'class': 'form-control', }),
            'isbn_number': forms.TextInput(attrs={'class': 'form-control', }),
            'number_of_pages': forms.NumberInput(attrs={'class': 'form-control', }),
            'link_to_cover': forms.URLInput(attrs={'class': 'form-control', }),
            'language': forms.TextInput(attrs={'class': 'form-control', }),
        }

        labels = {
            'title': 'Title',
            'author': 'Author',
            'date_published': 'Date Published',
            'isbn_number': 'ISBN Number',
            'number_of_pages': 'Number of Pages',
            'link_to_cover': 'Link to Cover',
            'language': 'Language',

        }
