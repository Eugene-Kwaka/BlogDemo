from django.shortcuts import render
from blog.models import Post

# Create your views here.

def home(request):
    # The filter function will only allow the posts with an active status to be displayed
    posts = Post.objects.filter(status=Post.ACTIVE)
    context = {
        'posts': posts
    }
    return render(request, 'core/home.html', context)

def about(request):
    about="here you can no more about us"
    return render(request, 'core/about.html', {'about':about})