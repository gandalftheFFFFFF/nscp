from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf
from .forms import LoginForm

# Create your views here.


def index(request):

    return render(request, 'preview.html', None)


def log_in(request):
    context = {}

    if request.method == 'POST':
        form = LoginForm(request.POST)
        context['form'] = form
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    context.update(csrf(request))
                    return render(request, 'preview.html', context)

            else:
                context['error'] = 'Invalid username or password.'
                return render(request, 'login.html', context)

        else:
            context['error'] = 'Invalid form input. Please try again.'
            return render(request, 'login.html', context)

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})