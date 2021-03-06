from django.db import models

from uuslug import uuslug

# Create your models here.

# class Post inherits from the standard Django Model() class
# It defines the database as well as each field:
# created_at, title, content - representing a single blog post

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    views = models.IntegerField(default=0)
    slug = models.CharField(max_length=100, unique=True)

    # method to return distinguishing information
    # about the object
    def __str__(self):
        # returns the complete object details
        # return "{0}/{1}/{2}/{3}\n".format(self.id, self.created_at,\
        #   self.title, self.content)
        return self.title   # returns only the Post title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self, max_length=100)
        super(Post, self).save(*args, **kwargs)
