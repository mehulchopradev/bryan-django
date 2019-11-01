from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # return HttpResponse('<html><body><b>Hello Worldddd</b></body></html>')
    return render(request, 'hello.html')

def home(request):
  return render(request, 'public/home.html')

def aboutus(request):
  return render(request, 'public/aboutus.html')

def contactus(request):
  # code to fetch the email and phone number data
  email = 'mehul@gmail.com'
  phone = '888768768'

  context_data = {
    'email_address': email,
    'phone': phone
  }

  # sending data to the view
  return render(request, 'public/contactus.html', context_data)