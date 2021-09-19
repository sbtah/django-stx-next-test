
from django.urls import path, include
from rest_framework import routers
from api.views import BookViewSet, book_list

# router = routers.DefaultRouter()
# router.register(r'books', book_list)


app_name = 'api'

urlpatterns = [
    path('api/', book_list, name='api'),
]
