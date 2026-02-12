from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post

class HomePageView(LoginRequiredMixin,ListView):
    model=Post
    template_name="posts/home.html"
    # context_object_name = <model>_list -> post_list


class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post
    template_name="posts/post_detail.html"
    # context_object_name=

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name="posts/post_create.html"
    fields = ["title","text"]
    success_url=reverse_lazy("posts_home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    template_name="posts/post_update.html"
    fields = ["title","text"]

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name="posts/post_delete.html"
    success_url=reverse_lazy("posts_home")
    
    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.author == self.request.user