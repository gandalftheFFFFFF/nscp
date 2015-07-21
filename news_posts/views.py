from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.

from .models import Post

def all_news(request):
    template = 'all_news.html'
    posts = get_list_or_404(Post)
    context = {
        'posts':posts,
    }

    return render(request, template, context)
