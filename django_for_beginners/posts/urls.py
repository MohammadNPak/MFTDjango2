from django.contrib import admin
from django.urls import path
from .views import ( 
    HomePageView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView)

urlpatterns = [
    path('posts/<int:pk>/delete', PostDeleteView.as_view(),name="post_delete"),
    path('posts/<int:pk>/update', PostUpdateView.as_view(),name="post_update"),
    path('posts/<int:pk>', PostDetailView.as_view(),name="posts_detail"),
    path('posts/new', PostCreateView.as_view(),name="post_new"),
    path('', HomePageView.as_view(),name="home"),


]