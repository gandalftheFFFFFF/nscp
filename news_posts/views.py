from django.shortcuts import render, get_object_or_404, get_list_or_404
from collections import defaultdict

# Create your views here.

from .models import Post


def news(request):
    template = 'news.html'
    try:
        post = Post.objects.latest('date')
    except Post.DoesNotExist:
        post = None
    try:
        older_posts = Post.objects.all()[1:4]
    except Post.DoesNotExist:
        older_posts = None
    context = {
        'post':post,
        'older_posts':older_posts,
    }
    return render(request, template, context)

def specific_post(request, post_slug):
    template = 'specific_news.html'
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        'post':post,
    }
    return render(request, template, context)


def archive(request):
    template = 'archive.html'
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None

    if posts:
        arch = {}
        for post in posts:
            year = post.date.year
            if year in arch:
                arch[year].append(post)
            else:
                arch[year] = [post,]
        #arc = defaultdict(list)
        #for post in posts:
            #year = post.date.year
            #arc[year].append(post)
    print(arch)

    context = {
        'posts':posts,
        'arc':arch,
    }
    return render(request, template, context)