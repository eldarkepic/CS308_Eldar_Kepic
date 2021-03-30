from django.shortcuts import render

# Create your views here.
from books.models import Book
from books.serializers import BookSerializer
from rest_framework import generics


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
