from django.db import models
from datetime import date, datetime

def handle_profile_pic_upload(student, file_name):
  return '{0}_{1}_{2}'.format(student.username, datetime.now(), file_name)

# Create your models here.
class Student(models.Model):
  # id
  username = models.CharField(max_length=50, null=False, unique=True)
  password = models.IntegerField(null=False)
  gender = models.CharField(max_length=1, null=False)
  country = models.CharField(max_length=10, null=True)
  profilepicpath = models.ImageField(null=True, blank=True, upload_to=handle_profile_pic_upload)

  # one to many (Book)
  # book_set

  def __str__(self):
      return 'Id : {0}\nUsername: {1}'.format(self.id, self.username)

class PublicationHouse(models.Model):
  # id
  name = models.CharField(max_length=30, null=False)
  ratings = models.IntegerField(null=False)

  # one to many (Book)
  # book_set

  def __str__(self):
      return self.name
  

class Book(models.Model):
  # id
  title = models.CharField(max_length=50, null=False)
  price = models.FloatField(null=True)
  pages = models.IntegerField(null=False)
  noofcopies = models.IntegerField(null=False)
  published_date = models.DateField(null=False)
  publication = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE)
  # students = models.ManyToManyField(Student)
  students = models.ManyToManyField(Student, through='BooksIssued')

  # many to one (PublicationHouse)
  # one to many (Review)
  # review_set

  # one to many (Student)

  def __str__(self):
      return self.title

class Review(models.Model):
  # id
  description = models.CharField(max_length=100, null=False)
  fullname = models.CharField(max_length=50, null=False)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)

  # many to one (Book)

class BooksIssued(models.Model):
  # id
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  issue_date = models.DateField(null=False, default=date.today())
  return_date = models.DateField(null=True)