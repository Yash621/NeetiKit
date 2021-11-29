from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.generic import ListView


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):


def about(request):
    return render(request, 'blog/about.html')
