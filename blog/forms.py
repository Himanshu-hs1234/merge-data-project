from django import forms

from .models import Post

from django.contrib.auth.forms import UserCreationForm

from .models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('name', 'username', 'phone_no', 'email', 'city', 'state', 'country','image')
