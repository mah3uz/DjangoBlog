from django.http import HttpResponse
from django.shortcuts import render

from blog_post.models import BlogPost


def index(request):
    posts = BlogPost.objects.all()
    context = {
        'posts': posts.order_by('-created_at'),
    }
    return render(request, 'index.html', context)