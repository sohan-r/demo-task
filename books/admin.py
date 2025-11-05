from django.contrib import admin
from .models import Book, ExternalPost

admin.site.register(Book)
admin.site.register(ExternalPost)
