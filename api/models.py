from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    author = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Title: {title}'
    