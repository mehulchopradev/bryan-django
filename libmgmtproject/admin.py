from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'pages', 'price')
  search_fields = ('title',)
  fields = ('title', 'pages', 'price', 'published_date', 'noofcopies')

# Register your models here.
admin.site.register(Book, BookAdmin)
