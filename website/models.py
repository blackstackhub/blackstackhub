from django.db import models
from django.contrib.auth.models import User

class Fanbase(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='fanbase_images/')
    link = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class BlogContent(models.Model):
    text = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='blog_content_files', null=True, blank=True)

    def __str__(self):
        if self.text:
            return f"{self.text[:5]}..."
        return ""

class Blog(models.Model):
    contents = models.ManyToManyField(BlogContent, related_name='blogs')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_content_files')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user_source = models.CharField(max_length=255)

    def __str__(self):
        return self.name
