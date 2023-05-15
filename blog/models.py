from django.db import models
from django.conf import settings
from django.utils import timezone
# from django_autoslug.fields import AutoSlugField
from django.contrib.auth.models import AbstractUser
# from autoslug import AutoSlugField
from django_extensions.db.fields import AutoSlugField
# from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length = 150, blank = True, null = True, unique = True)
    phone_no = models.CharField(max_length = 10, blank = True, null = True)
    email = models.CharField(max_length= 100, blank = True, null = True)
    city=models.CharField(max_length = 150, blank = True, null = True)
    state=models.CharField(max_length = 150, blank = True, null = True)
    country=models.CharField(max_length = 150, blank = True, null = True)
    image = models.ImageField(upload_to='image/', blank=True, null = True)
 
    def __str__(self):
        return self.username

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    
    def __str__(self):
        return self.name
    

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    thumbnail_image = models.ImageField(upload_to='thumbnail_image/', blank=True, null = True)
    featured_image = models.ImageField(upload_to='featured_image/', blank=True, null = True)

    def publish(self): 
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)
    


# class Book(models.Model):
#     title = models.CharField(db_column='title', max_length=100, blank=False)
#     description = models.TextField(db_column='description', max_length=1000, blank=False)
#     author = models.CharField(db_column='author', max_length=100, blank=False)
#     year = models.IntegerField(db_column='year',blank=False, default="current")
#     class Meta:
#         db_table = 'book'
#         verbose_name = 'Book'
#         verbose_name_plural = 'Books'
#     def __unicode__(self):
#         return self.title
#     def __str__(self):
#         return self.title
    
                              
# class Blog(models.Model):
#         title = models.CharField(max_length=120)
#         author = models.CharField(max_length=120)
#         date_of_publishing = models.DateField(auto_now_add=True)
#         content = models.TextField()
#         def __str__(self):
#             return self.title     



