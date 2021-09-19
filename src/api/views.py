from rest_framework import viewsets
from .serializers import BookSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from books.models import Book
from django.views.decorators.csrf import csrf_exempt


# Api Stuff.
class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


@csrf_exempt
def book_list(request):

    if request.method == 'GET':

        articles = Book.objects.all()
        serializer = BookSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)
