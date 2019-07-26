from django.db import models
from django.utils import timezone

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    text = models.TextField('')
    
    
    def summary(self):
        return self.body[:100]

class Shop(models.Model):
    title = models.CharField(max_length = 100)
    address = models.CharField(max_length = 300)
    instagram = models.CharField(max_length = 100)
    facebook = models.CharField(max_length = 100)
    time = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('homepage.Notice', related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.content

class Qna(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    text = models.TextField(default='')

    def summary(self):
        return self.body[:100]
