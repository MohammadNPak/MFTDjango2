from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post
from .forms import CommentForm


class HomePageView(LoginRequiredMixin,ListView):
    model=Post
    template_name="posts/home.html"
    # context_object_name = <model>_list -> post_list


class PostDetailViewGet(DetailView):
    model=Post
    template_name="posts/post_detail.html"
    # context_object_name=
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["comment_form"] = CommentForm()
        return contex

class PostDetailViewPost(SingleObjectMixin,FormView):
    model=Post
    form_class=CommentForm

    def post(self, request, *args: str, **kwargs) :
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def  form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return self.get_object().get_absolute_url()
        # return super().get_success_url()
    

class PostDetailView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        view = PostDetailViewGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostDetailViewPost.as_view()
        return view(request, *args, **kwargs)

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