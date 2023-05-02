from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('sign_up/', views.sign_up_request, name='signup'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name= 'logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),

]

