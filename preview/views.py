from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
from django.template.context_processors import csrf
from .forms import LoginForm, CreateUserForm, UserProfileForm

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

            print(user)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    context.update(csrf(request))
                    context['form'] = UserProfileForm()
                    return render(request, 'user_page.html', context)
                else:
                    context['error'] = 'The user has been disabled.'
                    return render(request, 'login.html', context)

            else:
                context['error'] = 'Invalid username or password.'
                return render(request, 'login.html', context)

        else:
            context['error'] = 'Invalid form input. Please try again.'
            return render(request, 'login.html', context)

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return render(request, 'user_page.html', None)


def create_user(request):
    context = {}

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        password_validation = request.POST['password_validation']
        context['form'] = form

        if form.is_valid() and password == password_validation:
            if User.objects.filter(username=username).exists():
                context['error'] = 'Username is already taken.'
                return render(request, 'create_user.html', context)
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                )
                user_profile = UserProfile(user=user)
                user_profile.save()
                user.save()
                return render(request, 'create_user_success.html', context)
        else:
            if password != password_validation:
                context['error'] = 'The passwords are not identical.'
            elif not form.is_valid():
                context['error'] = 'Invalid form input.'
            return render(request, 'create_user.html', context)
    else:
        context['form'] = CreateUserForm()
        return render(request, 'create_user.html', context)


def user_page(request):
    context = {}
    user = request.user

    if user.is_authenticated():
            user_profile = UserProfile.objects.get(user=user)
            user_info = user_profile.get_info()
            context['form'] = UserProfileForm(user_info)

            if request.method == 'POST':
                # Get the new data into the form
                context['form'] = UserProfileForm(request.POST)

                # Update user profile data
                email = request.POST['email']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                company = request.POST['company']

                user_profile.update(email, first_name, last_name, company)

                return render(request, 'user_page.html', context)

            else:
                return render(request, 'user_page.html', context)

    return render(request, 'user_page.html', context)