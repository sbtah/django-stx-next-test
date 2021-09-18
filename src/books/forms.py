from .models import Book
from django import forms


class BookForm(forms.ModelForm):

    class Meta:

        model = Book

        fields = ('title', 'author', 'date_published', 'isbn_number',
                  'number_of_pages', 'link_to_cover', 'language')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'date_published': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'format': '%Y%m%d'}),
            'isbn_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN Number'}),
            'number_of_pages': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Pages'}),
            'link_to_cover': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'http://www.example.com'}),
            'language': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Language'}),
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


# class SearchBook(forms.Form):

#     keyword = forms.CharField(label='keyword', max_length=100)


class SearchBook(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['keyword'].widget.attrs.update(
            {'class': 'form-control'})

    keyword = forms.CharField(label='keyword', max_length=100)

    class Meta:

        model = Book
        fields = ["keyword"]
