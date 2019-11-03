from django.urls import path
from .views import home, register, register_user, auth

# libmgmt/

app_name = 'libapp'

urlpatterns = [
    path('home/', home, name='home'),
    path('sign-up/', register, name='register'),
    path('register/', register_user, name="register_user"),
    path('auth/', auth, name='auth')
]
