from django.contrib import admin
from .models import Post

from .models import User


from django.shortcuts import render
from .models import Post, Category, Author

# Register your models here.


admin.site.register(Post)

admin.site.register(User)


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)


