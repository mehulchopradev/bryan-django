from django import forms

class LoginForm(forms.Form):
  username = forms.CharField(label='', widget=forms.TextInput(attrs={
    'placeholder': 'Enter username'
  }), error_messages={'required': 'Username is required'})
  password = forms.IntegerField(label='', widget=forms.PasswordInput(attrs={
    'placeholder': 'Enter password'
  }))