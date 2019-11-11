from django import forms
from .models import Student

class LoginForm(forms.Form):
  username = forms.CharField(label='', widget=forms.TextInput(attrs={
    'placeholder': 'Enter username'
  }), error_messages={'required': 'Username is required'})
  password = forms.IntegerField(label='', widget=forms.PasswordInput(attrs={
    'placeholder': 'Enter password'
  }))

''' class RegisterForm(forms.Form):
  username = forms.CharField(label='', widget=forms.TextInput(attrs={
    'placeholder': 'Enter username'
  }), error_messages={'required': 'Username is required'})
  password = forms.IntegerField(label='', widget=forms.PasswordInput(attrs={
    'placeholder': 'Enter password'
  }))
  country = forms.ChoiceField(choices=(('IN', 'India'), ('US', 'America')), label='Country')
  gender = forms.ChoiceField(widget=forms.RadioSelect(), choices=(('M', 'Male'), ('F', 'Female')), label='Gender') '''

class RegisterForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ('username', 'password', 'country', 'gender', 'profilepicpath')

    labels = {
      'username': '',
      'password': ''
    }

    widgets = {
      'username': forms.TextInput(attrs={
        'placeholder': 'Enter username'
      }),
      'password': forms.PasswordInput(attrs={
        'placeholder': 'Enter password'
      }),
    }
  
  def __init__(self, *args, **kwargs):
    # code to query the backend service/ database to get countries and genders
    countries = (('IN', 'India'), ('US', 'America'))
    genders = (('M', 'Male'), ('F', 'Female'))

    super().__init__(*args, **kwargs)

    self.fields['country'] = forms.ChoiceField(choices=countries)
    self.fields['gender'] = forms.ChoiceField(widget=forms.RadioSelect(), choices=genders)