# basic rendering tools
from django.shortcuts import render, redirect
from django.http import HttpResponse

# user authentication
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test,
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
)

# imports from this app
from main.models import Post
from main.forms import PostForm


def index(request):
    return render(request, 'index.html')


def register(request):

    # if a user is already logged in, redirect to the front page
    if request.user.is_authenticated():
        return redirect('index')

    # save a blank user creation form in the context
    context = {'user_creation_form': UserCreationForm}

    # if the hit to this URL was a POST (not GET or DELETE or whatever)
    if request.method == 'POST':

        # get and check if the filled form is valid
        filled_user_creation_form = UserCreationForm(request.POST)
        if filled_user_creation_form.is_valid():

            # create a new user object with the form information
            user = filled_user_creation_form.save()

            # authenticate the new user against the database (formality)
            user = authenticate(username=user.username,
                                password=request.POST['password1'])

            # log the new user into the site and redirect to front page
            auth_login(request, user)
            return redirect('index')

        # if the filled form is invalid
        else:

            # save error message and invalid form to be passed back for editing
            context['error_on_create'] = True
            context['user_creation_form'] = filled_user_creation_form

    # if the request wasn't a POST or the filled form was invalid, render the
    # registration page (with a blank form in the first case and the invalid
    # form in the second case).
    return render(request, 'register.html', context)


def login(request):

    # if a user is already logged in, redirect to the front page
    if request.user.is_authenticated():
        return redirect('index')

    # if the hit to this URL was a POST (not GET or DELETE or whatever)
    if request.method == 'POST':

        # attempt to authenticate the user
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])

        # if ther user is found in the database
        if user is not None:

            # and the user's account is active
            if user.is_active:

                # then go ahead and log the user in and redirect to front page
                auth_login(request, user)
                # return render(request, 'index.html', {})
                return redirect('index')

            # if the user's account is not active
            else:

                # reload the login page and display error message
                context['error'] = 'Account deactivated.'
                return render(request, 'login.html', context)

        # if this user doesn't exist in the database
        else:

            # reload the login page and display error message
            context['error'] = 'Username or password not found.'
            return render(request, 'login.html', context)

    # if the request method was not POST
    else:
        return render(request, 'login.html', {})


def logout(request):
    auth_logout(request)
    return redirect('index')


def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save()
        return redirect('index')
    else:
        message = form.errors
        return render(request, 'index.html', {'message': message})


def get_posts(request):
    page = int(request.GET.get('page', 0))
    page_size = 10
    start = page * page_size
    end = (page+1) * page_size
    posts = Post.objects.all().order_by('-created')[start:end]
    if len(posts) > 0:
        return render(request, 'posts-page.html', {'posts': posts})
    else:
        return HttpResponse('')
