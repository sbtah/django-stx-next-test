from django.urls import path
from .views import book_list, book_create, book_update


app_name = 'books'

urlpatterns = [
    path('', book_list, name='book-list'),
    path('create/', book_create, name='book-create'),
    path('update/<int:pk>', book_update, name='book-update'),
]
