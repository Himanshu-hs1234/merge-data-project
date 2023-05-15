from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Post, User,Comment



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'category', 'tag', 'text', 'thumbnail_image', 'featured_image')


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone_no', 'email', 'city', 'state', 'country','image')

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone_no', 'email', 'city', 'state', 'country','image')




 
    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     self.fields['first_name'].widget.attrs = {'placeholder': ' first_name','class':'form-control'}
    #     self.fields['last_name'].widget.attrs = {'placeholder': 'last_name','class':'form-control'}
    #     self.fields['username'].widget.attrs = {'placeholder': 'username','class':'form-control'}
    #     self.fields['phone_no'].widget.attrs = {'placeholder': 'phone_no','class':'form-control'}
    #     self.fields['email'].widget.attrs = {'placeholder': 'email','class':'form-control'}
    #     self.fields['city'].widget.attrs = {'placeholder': 'city','class':'form-control'}
    #     self.fields['state'].widget.attrs = {'placeholder': 'state','class':'form-control'}
    #     self.fields['country'].widget.attrs = {'placeholder': 'country', 'class':'form-control'}
    #     self.fields['image'].widget.attrs = {'placeholder': 'image', 'class':'form-control', 'rows':'7'}



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


        