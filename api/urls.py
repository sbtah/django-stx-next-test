
from django.urls import path, include
from rest_framework import routers
from api.views import BookViewSet, book_list

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)


app_name = 'api'

urlpatterns = [
    path('api/', include(router.urls), name='api'),
]
