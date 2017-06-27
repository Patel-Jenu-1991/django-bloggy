from django.db import models

# Create your models here.

# class Post inherits from the standard Django Model() class
# It defines the database as well as each field:
# created_at, title, content - representing a single blog post

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
