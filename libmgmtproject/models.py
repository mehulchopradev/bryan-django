from django.db import models

# Create your models here.
class Student(models.Model):
  # id
  username = models.CharField(max_length=50, null=False, unique=True)
  password = models.IntegerField(null=False)
  gender = models.CharField(max_length=1, null=False)
  country = models.CharField(max_length=10, null=True)

  def __str__(self):
      return 'Id : {0}\nUsername: {1}'.format(self.id, self.username)

class Book(models.Model):
  # id
  title = models.CharField(max_length=50, null=False)
  price = models.FloatField(null=True)
  pages = models.IntegerField(null=False)
  noofcopies = models.IntegerField(null=False)
  published_date = models.DateField(null=False)

  def __str__(self):
      return self.title
  
  
