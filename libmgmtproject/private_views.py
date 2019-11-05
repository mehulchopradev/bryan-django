from django.shortcuts import render, reverse
from .models import Book, Student
from django.http import HttpResponse, HttpResponseRedirect

def welcome(request):
  if 'username' not in request.session:
    return HttpResponseRedirect(reverse('libapp:home'))

  books = Book.objects.order_by('price')
  for book in books:
    if book.noofcopies == 0:
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

  return HttpResponseRedirect(reverse('libapp:home'))

def issue_book(request, bookid):
  if 'username' not in request.session:
    return HttpResponseRedirect(reverse('libapp:home'))

  student = Student.objects.get(pk=request.session['userid'])
  book = Book.objects.get(pk=bookid)

  book.students.add(student)

  return HttpResponseRedirect(reverse('libapp:welcome'))

def return_book(request, bookid):
  if 'username' not in request.session:
    return HttpResponseRedirect(reverse('libapp:home'))
  
  book = Book.objects.get(pk=bookid)
  student_id = request.session['userid']
  book.students.remove(student_id)

  return HttpResponseRedirect(reverse('libapp:welcome'))