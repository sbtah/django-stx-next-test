from django.urls import path
from .views import book_list, book_create, book_update, book_delete


app_name = 'books'

urlpatterns = [
    path('', book_list, name='book-list'),
    path('create/', book_create, name='book-create'),
    path('update/<int:pk>', book_update, name='book-update'),
    path('delete/<int:pk>', book_delete, name='book-delete'),
]
