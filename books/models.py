from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=250)
    publisher = models.CharField(max_length=100)
    publicationDate = models.DateTimeField(auto_now_add=True)
    numberOfPages = models.IntegerField()

    def __str__(self):
        return self.title
