from django.urls import path
from .views import home, register, register_user, auth
from .private_views import welcome, get_book_details, logout, issue_book, return_book

# libmgmt/

app_name = 'libapp'

urlpatterns = [
    path('home/', home, name='home'),
    path('sign-up/', register, name='register'),
    path('register/', register_user, name="register_user"),
    path('auth/', auth, name='auth'),
    path('welcome/', welcome, name='welcome'),
    path('books/<int:bookid>', get_book_details, name='getbook'),
    path('logout/', logout, name='logout'),
    path('issue-book/<int:bookid>', issue_book, name='issuebook'),
    path('return-book/<int:bookid>', return_book, name='returnbook')
]
