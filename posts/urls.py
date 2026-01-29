from django.contrib import admin
from django.urls import path
from .views import ( 
    HomePageView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView)

urlpatterns = [
    path('/<int:pk>/update', PostDeleteView.as_view(),name="post_delete"),
    path('/<int:pk>/delete', PostUpdateView.as_view(),name="post_update"),
    path('/<int:pk>', PostDetailView.as_view(),name="posts_detail"),
    path('', HomePageView.as_view(),name="posts_home"),
    path('/new', PostCreateView.as_view(),name="post_new"),


]