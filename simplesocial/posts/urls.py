from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name ='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/(?P<username>[-\w]+)/(?P<pk>\d+/)', views.PostDetail.as_view(), name='single'),
    path('by/(?P<username>[-\w]+)/', views.UserPosts.as_view(), name='for_user'),
    path('by/(?P<username>[-\w]+)/(?P<pk>\d+/)',views.PostDetail.as_view(), name='detail'),
    path('delete/(?<P<pk>\d+/)',views.DeletePost.as_view(), name='delete'),



]
