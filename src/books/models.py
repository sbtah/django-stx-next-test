from django.db import models
from django.urls import reverse


class Book(models.Model):

    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    date_published = models.DateField()
    isbn_number = models.CharField(max_length=120)
    number_of_pages = models.PositiveIntegerField()
    link_to_cover = models.URLField()
    language = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.title} - {self.author}"

    def get_absolute_url(self):

        return reverse('books:book-detail', kwargs={
            'pk': self.pk,
        })
