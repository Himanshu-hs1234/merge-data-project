from django.db import models
from django.conf import settings
from django.utils import timezone
# from django_autoslug.fields import AutoSlugField
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length = 150, blank = True, null = True)
    phone_no = models.CharField(max_length = 10, blank = True, null = True)
    email = models.CharField(max_length= 100, blank = True, null = True)
    city=models.CharField(max_length = 150, blank = True, null = True)
    state=models.CharField(max_length = 150, blank = True, null = True)
    country=models.CharField(max_length = 150, blank = True, null = True)
    image = models.ImageField(upload_to='media/', blank=True, null = True)
 
    def __str__(self):
        return self.email

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=name)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=name)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from=title)
    thumbnail = models.ImageField(upload_to='thmbnail/', null=True, blank=True) 


    def publish(self): 
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
