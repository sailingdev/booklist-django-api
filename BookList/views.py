from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

from .models import (
    WriterModel,
    GenreModel,
    BookModel
)

from .serializers import (
    WriterSerializer,
    GenreSerializer,
    BookSerializer
)

class WriterList(APIView):
    def get(self, request, format=None):
        writers = WriterModel.objects.all()
        serializer = WriterSerializer(writers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WriterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WriterDetail(APIView):
    def get_object(self, pk):
        try:
            return WriterModel.objects.get(pk=pk)
        except WriterModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        writer = self.get_object(pk)
        serializer = WriterSerializer(writer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        writer = self.get_object(pk)
        serializer = WriterSerializer(writer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        writer = self.get_object(pk)
        writer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GenreList(APIView):
    def get(self, request, format=None):
        genres = GenreModel.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenreDetail(APIView):
    def get_object(self, pk):
        try:
            return GenreModel.objects.get(pk=pk)
        except GenreModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookList(APIView, PageNumberPagination):

    def get_queryset(self):
        queryset = BookModel.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__contains=name)
        genres = self.request.query_params.get('genres')
        if genres is not None:
            genres_list = genres.split(',')
            book_id_list = []
            for genre in genres_list:
                obj = GenreModel.objects.get(id=genre)
                for book in obj.bookmodel_set.all():
                    book_id_list.append(book.id)
            queryset = queryset.filter(pk__in=list(dict.fromkeys(book_id_list)))
        return queryset

    def get(self, request, format=None):

        books = self.get_queryset()
        results = self.paginate_queryset(books, request, view=self)
        serializer = BookSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return BookModel.objects.get(pk=pk)
        except BookModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
