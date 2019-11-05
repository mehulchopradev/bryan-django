from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

def welcome(request):
  books = Book.objects.order_by('price')
  context_data = {
    'booklist': books
  }
  return render(request, 'libmgmtproject/private/welcome.html', context_data)

def get_book_details(request, bookid):
  book = Book.objects.get(pk=bookid)
  return render(request, 'libmgmtproject/private/book.html', {
    'book': book
  })