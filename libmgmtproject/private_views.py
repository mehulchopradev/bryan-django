from django.shortcuts import render, reverse
from .models import Book, Student, BooksIssued
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PublicationHouseSerializer
from .models import PublicationHouse

def welcome(request):
  if 'username' not in request.session:
    return HttpResponseRedirect(reverse('libapp:home'))

  books = Book.objects.order_by('price')
  student = Student.objects.get(pk=request.session['userid'])

  for book in books:
    ''' if book.noofcopies == 0:
      book.cannotissue = True # we can add dervied attributes to a model
    else:
      student = Student.objects.get(pk=request.session['userid'])
      students_bookissued = book.students.all()
      if student in students_bookissued:
        book.cannotissue = False
        book.alreadyissued = True
      else:
        book.alreadyissued = False
        if len(students_bookissued) == book.noofcopies:
          book.cannotissue = True
        else:
          book.cannotissue = False '''
    if book.noofcopies == 0:
      book.cannotissue = True
    else:
      booksissued = BooksIssued.objects.filter(book=book, student=student, return_date=None)
      if booksissued:
        book.cannotissue = False
        book.alreadyissued = True
      else:
        book.alreadyissued = False
        other_students = BooksIssued.objects.filter(book=book, return_date=None)
        if len(other_students) == book.noofcopies:
          book.cannotissue = True
        else:
          book.cannotissue = False

  username = request.session['username']
  context_data = {
    'booklist': books,
    'username': username
  }
  return render(request, 'libmgmtproject/private/welcome.html', context_data)

def get_book_details(request, bookid):
  if 'username' not in request.session:
    return HttpResponseRedirect(reverse('libapp:home'))

  book = Book.objects.get(pk=bookid)
  username = request.session['username']
  return render(request, 'libmgmtproject/private/book.html', {
    'book': book,
    'username': username
  })

def logout(request):
  session = request.session
  session.flush()

  # return HttpResponseRedirect(reverse('libapp:home'))
  return HttpResponseRedirect(reverse('libapp:login'))

def issue_book(request, bookid):
  if 'username' not in request.session:
    return HttpResponseRedirect(reverse('libapp:home'))

  student = Student.objects.get(pk=request.session['userid'])
  book = Book.objects.get(pk=bookid)

  # book.students.add(student)
  obj = BooksIssued(student=student, book=book)
  obj.save()

  return HttpResponseRedirect(reverse('libapp:welcome'))

def return_book(request, bookid):
  if 'username' not in request.session:
    return HttpResponseRedirect(reverse('libapp:home'))
  
  book = Book.objects.get(pk=bookid)
  student_id = request.session['userid']
  # book.students.remove(student_id)
  student = Student.objects.get(pk=student_id)

  booksissued = BooksIssued.objects.get(student=student, book=book)
  booksissued.return_date = date.today()
  booksissued.save()

  return HttpResponseRedirect(reverse('libapp:welcome'))

def get_profile_pic(request):
  if 'username' not in request.session:
    return HttpResponseRedirect(reverse('libapp:home'))

  student = Student.objects.get(pk=request.session['userid'])
  file_path = student.profilepicpath.path
  with open(file_path, mode='rb') as fp:
    return HttpResponse(fp.read(), content_type='image/*')

class PublicationListApiView(ListAPIView):
  serializer_class = PublicationHouseSerializer
  queryset = PublicationHouse.objects.all()

class PublicationRetrieveApiView(RetrieveAPIView):
  serializer_class = PublicationHouseSerializer
  queryset = PublicationHouse.objects.all()

class PublicationApiView(ModelViewSet):
  serializer_class = PublicationHouseSerializer
  # queryset = PublicationHouse.objects.order_by('-ratings')

  def get_queryset(self):
    queryparams = self.request.query_params
    if 'ratings' in queryparams:
      return PublicationHouse.objects.filter(ratings=int(queryparams['ratings']))
    
    return PublicationHouse.objects.order_by('-ratings')