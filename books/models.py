from django.db import models
from django.urls import reverse


class Book(models.Model):
    """
    A model for Book.
    """

    title = models.CharField(max_length=120, blank=True, null=True)
    author = models.CharField(max_length=120, blank=True, null=True)
    date_published = models.CharField(max_length=12, blank=True, null=True)
    isbn_number = models.CharField(max_length=120, blank=True, null=True)
    number_of_pages = models.PositiveIntegerField(blank=True, null=True)
    link_to_cover = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=120, blank=True, null=True)

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

    # This redirects delete function.
    def get_delete_url(self):

        return reverse('books:book-delete', kwargs={
            'pk': self.pk,
        })
