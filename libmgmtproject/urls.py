from django.urls import path, include
from .views import home, register, register_user, auth, loginform, LoginView, LoginFormView, RegisterFormView
from .private_views import welcome, get_book_details, logout, issue_book, return_book, get_profile_pic, PublicationListApiView, PublicationRetrieveApiView\
    , PublicationApiView
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('publication-houses', PublicationApiView, 'publication-houses')

# libmgmt/

app_name = 'libapp'

urlpatterns = [
    path('home/', home, name='home'),
    path('sign-up-new/', TemplateView.as_view(template_name='libmgmtproject/public/register.html')),
    path('sign-up/', register, name='register'),
    path('register/', register_user, name="register_user"),
    path('auth/', auth, name='auth'),
    path('welcome/', welcome, name='welcome'),
    path('books/<int:bookid>', get_book_details, name='getbook'),
    path('logout/', logout, name='logout'),
    path('issue-book/<int:bookid>', issue_book, name='issuebook'),
    path('return-book/<int:bookid>', return_book, name='returnbook'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('register-here/', RegisterFormView.as_view(), name='registerhere'),
    path('profile-pic/', get_profile_pic, name='profilepic'),
    path('', include(router.urls))
    # path('login/', loginform, name='login')
]

'''

 path('publication-houses/', PublicationListApiView.as_view()),
    path('publication-houses/<int:pk>/', PublicationRetrieveApiView.as_view())

'''
