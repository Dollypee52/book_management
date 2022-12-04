from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import connection, transaction

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from . filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend


from new_app.models import Book, Publisher
from new_app.serializer import BookSerializer, PublisherSerializer
from .pagination import BookPagination


def index(request):
    context = [1, 2, 3]
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua."
    return render(request, 'new_app/index.html',
                  context={'obj': context, "name": "tola", "is_major": False, "text": text})


def about(request):
    return render(request, 'new_app/about.html')


def redirect(request):
    return HttpResponseRedirect(reverse('new_app:index'))


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'isbn']
    ordering_fields = ['title','price']
    ordering = ['title']
    pagination_class = BookPagination
    # pagination_class = PageNumberPagination


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


# generic way
# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class PublisherList(ListCreateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = BookSerializer
#
#
# class PublisherDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer

# def book_details(request, pk):
# try:
#     book = Book.objects.get(pk=pk)
#     return render(request, "new_app/book_details.html", {"book": book})
# except Book.DoesNotExist:
#     return HttpResponse('Goodbye')
# book = Book.objects.get(pk=pk)
# return render(request, 'new_app/book_details.html', {'book': book})


# def book_list(request):
# books = Book.objects.all()
# books = Book.objects.filter(genre='ROMANCE')

# books = Book.objects.all()
# books = Book.objects.defer('publisher').all()
# books = Book.objects.raw('select * from new_app_book')
# books = Book.objects.selected_related('title', 'price')

# books = Book.objects.filter(publisher__id__in=(1, 7, 3)).only('title', 'price')
# return render(request, "new_app/book_list.html", {"books": books})


# class wAy

class BookList(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class BookDetail(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book)
#
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class PublisherList(APIView):
#     def get(self, request):
#         queryset = Publisher.objects.all()
#         serializer = PublisherSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PublisherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class PublisherDetail(APIView):
#     def get(self, request, pk):
#         publisher = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(publisher)
#
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         publisher = get_object_or_404(Publisher, pk=pk)
#         serializer = PublisherSerializer(publisher, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         publisher = get_object_or_404(Publisher, pk=pk)
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# api_view way

# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request == 'GET':
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request == 'POST':
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
# def book_detail(request, pk):
#     # book = Book.objects.get(pk=pk)
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#
#         return Response(serializer.data)
#     elif request.method in ('GET', 'PATCH'):
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def publisher_list(request):
#     # queryset = Publisher.objects.all()
#     # serializer = PublisherSerializer(queryset, many=True)
#     # return Response(serializer.data)
#     if request == 'GET':
#         queryset = Publisher.objects.all()
#         serializer = PublisherSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request == 'POST':
#         serializer = PublisherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
# def publisher_detail(request, pk):
#     # publisher = get_object_or_404(Publisher,pk=pk)
#     # serializer = PublisherSerializer(publisher)
#     # return  Response(serializer.data)
#     publisher = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = PublisherSerializer(publisher)
#
#         return Response(serializer.data)
#     elif request.method in ('GET', 'PATCH'):
#         serializer = PublisherSerializer(publisher, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'DELETE':
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
