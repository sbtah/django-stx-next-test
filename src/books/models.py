from django.db import models
from django.urls import reverse


class Book(models.Model):
    """
    A model for Book.
    """

    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    date_published = models.DateField()
    isbn_number = models.CharField(max_length=120)
    number_of_pages = models.PositiveIntegerField()
    link_to_cover = models.URLField()
    language = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.title} - {self.author}"

    # This doesn't work yet. Dunno if I should make a detail view for this model?
    def get_absolute_url(self):

        return reverse('books:book-detail', kwargs={
            'pk': self.pk,
        })

    # This redirects to update view for book model.
    def get_update_url(self):

        return reverse('books:book-update', kwargs={
            'pk': self.pk,
        })
