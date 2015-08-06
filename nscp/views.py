__author__ = 'niels'
from django.shortcuts import render
from django.core.mail import send_mail
from news_posts.models import Post


def index(request):
    try:
        post = Post.objects.latest('date')
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post,
    }

    return render(request, 'base.html', context)

def about(request):
    return render(request, 'about.html', context=None)


def contact(request):
    return render(request, 'contact.html', None)


def contact_by_form(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name'):
            errors.append('Please enter a name')
        if not request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Please enter an email')
        if not request.POST.get('message'):
            errors.append('Please enter a message')
        if not errors:
            send_mail('[NSCP CONTACT FORM]',
                request.POST['message'],
                request.POST.get('email'),
                ['niels@nscp.dk'],
            )
            return render(request, 'contact_thanks.html', {'name': request.POST.get('name')})
    return render(request, 'contact.html', {'errors': errors})
