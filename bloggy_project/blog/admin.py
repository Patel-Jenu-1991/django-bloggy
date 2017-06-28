from django.contrib import admin
from blog.models import Post

# Customize admin views here

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views')

# Register your models here.

admin.site.register(Post, PostAdmin)
