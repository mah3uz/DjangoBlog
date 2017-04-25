from django.http import HttpResponse
from django.shortcuts import render

from blog_post.models import BlogPost


def index(request):
    posts = BlogPost.objects.all()
    if 'category' in request.GET:
        posts = posts.filter(category=int(request.GET.get('category')))

    context = {
        'posts': posts.order_by('-created_at'),
    }

    return render(request, 'index.html', context)

def view_post(request, pk):
    post = BlogPost.objects.get(pk=pk)

    return render(request, 'post_view.html', {'post': post})