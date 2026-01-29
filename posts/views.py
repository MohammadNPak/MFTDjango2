from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post


class HomePageView(ListView):
    model=Post
    template_name="posts/home.html"
    # context_object_name = <model>_list -> post_list


class PostDetailView(DetailView):
    model=Post
    template_name="posts/post_detail.html"
    # context_object_name=

class PostCreateView(CreateView):
    model=Post
    template_name="posts/post_create.html"
    fields = ["title","text","author"]
    success_url=reverse_lazy("posts_home")

class PostUpdateView(UpdateView):
    model=Post
    template_name="posts/post_update.html"
    fields = ["title","text"]

class PostDeleteView(DeleteView):
    model=Post
    template_name="posts/post_delete.html"
    success_url=reverse_lazy("posts_home")