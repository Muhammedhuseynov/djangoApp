from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Images(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='media',blank=True,null=True)

class Comm(models.Model):
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=150)

    def __str__(self):
        return self.comment
    
    