from django.shortcuts import render
from django.http import HttpResponse

from main.models import Post
from main.forms import PostForm


def index(request):
    return render(request, 'index.html')


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
