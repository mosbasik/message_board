# basic rendering tools
from django.shortcuts import render, redirect
from django.http import HttpResponse

# user authentication
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login

# imports from this app
from main.models import Post
from main.forms import PostForm


def index(request):
    return render(request, 'index.html')



def login(request):

    # if the user is already logged in, redirect them to the front page
    if request.user.is_authenticated():
        return redirect('index')

    # save a blank user creation form in the context
    context = {'user_creation_form': UserCreationForm}

    # if the hit to this URL was a POST (not GET or DELETE or whatever)
    if request.method == 'POST':

        # if the user filled out the login form
        if request.POST['type'] == 'login':

            # attempt to authenticate the user
            print request.POST['username']

            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])

            # if ther user is found in the database
            if user is not None:

                # and the user's account is active
                if user.is_active:

                    # then go ahead and log the user in and load the index
                    auth_login(request, user)
                    return render(request, 'index.html', context)


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

        # if the user filled out the registration form
        else:
            pass

    # if the request method was not POST
    else:
        return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('index')


def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save()
        message = 'Post successful'
    else:
        message = form.errors
    return render(request, 'index.html', {'message': message})


def get_posts(request):
    page = int(request.GET.get('page', 0))
    page_size = 3
    start = page * page_size
    end = (page+1) * page_size
    posts = Post.objects.all().order_by('-created')[start:end]
    if len(posts) > 0:
        return render(request, 'posts-page.html', {'posts': posts})
    else:
        return HttpResponse('')
