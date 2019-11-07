from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView
from .models import Student
from .forms import LoginForm
from django.db.utils import IntegrityError

# Create your views here.

def home(request):
  loginform = LoginForm()
  return render(request, 'libmgmtproject/public/home.html', {
    'form': loginform
  })

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
    # remember username and id of the user in the session
    student = students[0]

    session = request.session
    session['username'] = username
    session['userid'] = student.id

    return HttpResponseRedirect(reverse('libapp:welcome'))
  return HttpResponseRedirect(reverse('libapp:home'))

def loginform(request):
  if request.method == 'GET':
    loginform = LoginForm()
  else:
    loginform = LoginForm(request.POST)
    if loginform.is_valid():
      data = loginform.cleaned_data
      students = Student.objects.filter(**data)
      if students:
        # remember username and id of the user in the session
        student = students[0]

        session = request.session
        session['username'] = data['username']
        session['userid'] = student.id

        return HttpResponseRedirect(reverse('libapp:welcome'))
      return HttpResponseRedirect(reverse('libapp:login'))

  return render(request, 'libmgmtproject/public/home.html', {
    'form': loginform
  })

class LoginView(View):
  def get(self, request):
    loginform = LoginForm()
    return render(request, 'libmgmtproject/public/home.html', {
      'form': loginform
    })

  def post(self, request):
    loginform = LoginForm(request.POST)
    if loginform.is_valid():
      data = loginform.cleaned_data
      students = Student.objects.filter(**data)
      if students:
        # remember username and id of the user in the session
        student = students[0]

        session = request.session
        session['username'] = data['username']
        session['userid'] = student.id

        return HttpResponseRedirect(reverse('libapp:welcome'))
      return HttpResponseRedirect(reverse('libapp:login'))

    return render(request, 'libmgmtproject/public/home.html', {
      'form': loginform
    })

class LoginFormView(FormView):
  template_name = 'libmgmtproject/public/home.html'
  form_class = LoginForm

  def form_valid(self, form):
    data = form.cleaned_data
    students = Student.objects.filter(**data)
    if students:
      # remember username and id of the user in the session
      student = students[0]

      session = self.request.session
      session['username'] = data['username']
      session['userid'] = student.id

      return HttpResponseRedirect(reverse('libapp:welcome'))
    return HttpResponseRedirect(reverse('libapp:login'))