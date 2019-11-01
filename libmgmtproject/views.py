from django.shortcuts import render
from django.http import HttpResponse

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

  # insert this data in the database TODO:

  print(username, password, gender, country)
  return HttpResponse('Hey registered!')
