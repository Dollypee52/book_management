from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db import connection, transaction

# Create your views here.
from new_app.models import Book


def index(request):
    context = [1,2,3]
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua."
    return render(request,'new_app/index.html', context={'obj': context, "name": "tola", "is_major":False, "text":text})

def about(request):
    return render(request,'new_app/about.html')

def redirect(request):
    return HttpResponseRedirect(reverse('new_app:index'))


def book_details(request,pk):
    # try:
    #     book = Book.objects.get(pk=pk)
    #     return render(request, "new_app/book_details.html", {"book": book})
    # except Book.DoesNotExist:
    #     return HttpResponse('Goodbye')
    book = Book.objects.get(pk=pk)
    return render(request,'new_app/book_details.html', {'book':book})


def book_list(request):
    # books = Book.objects.all()
    # books = Book.objects.filter(genre='ROMANCE')

     # books = Book.objects.all()
     # books = Book.objects.defer('publisher').all()
     # books = Book.objects.raw('select * from new_app_book')
     # books = Book.objects.selected_related('title', 'price')


     books = Book.objects.filter(publisher__id__in=(1,7,3)).only('title','price')
     return render(request, "new_app/book_list.html", {"books": books})