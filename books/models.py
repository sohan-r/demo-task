from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, default="General")
    published_date = models.DateField(null=True, blank=True)
    pages = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ExternalPost(models.Model):
    external_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    fetched_at = models.DateTimeField(auto_now_add=True)
