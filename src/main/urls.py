from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from books.views import api_get


urlpatterns = [
    path('test/', api_get),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls', namespace='books')),
    path('', include('api.urls', namespace='api-list')),
]


# Adding STATIC and MEDIA
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Books"
