from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from django.db.utils import IntegrityError

# Create your views here.

def home(request):
  return render(request, 'libmgmtproject/public/home.html')

def register(request):
  return render(request, 'libmgmtproject/public/register.html')

def register_user(request):
  data = request.POST
  username = data['username']
  password = data['password']
  gender = data['gender']
  country = data['country']

  student = Student(username=username, password=password, gender=gender, country=country)

  try:
    student.save()
  except IntegrityError:
    return HttpResponse('Username already exists')

  # print(username, password, gender, country)
  # redirecting the user to a different url
  return HttpResponseRedirect(reverse('libapp:home'))

def auth(request):
  username = request.POST['username']
  password = int(request.POST['password'])

  students = Student.objects.filter(username=username, password=password)
  if students:
    return HttpResponse('Valid user')
  return HttpResponseRedirect(reverse('libapp:home'))
