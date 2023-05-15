from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('post/new/', views.post_new, name ='post_new'),
    path("category/<str:category>/", views.category, name='category'),
    path("tag/<str:tag>/", views.tag, name = 'tags'),
    path('post/<str:slug>/', views.post_detail, name = 'post_detail'),
    path('post/<str:slug>/edit/', views.post_edit, name = 'post_edit'),
    path('sign_up/', views.sign_up_request, name = 'signup'),
    path('login/', views.login_request, name = 'login'),
    path('logout/', views.logout_request, name = 'logout'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('profile/', views.profile, name = 'profile'),
    path('', views.post_list, name='post_list'),
   
]



