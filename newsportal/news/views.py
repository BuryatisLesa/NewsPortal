from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Post


class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_news.html'
    context_object_name = 'post'

