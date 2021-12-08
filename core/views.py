from django.db.models.fields import TextField
from django.http.response import HttpResponse
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

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")