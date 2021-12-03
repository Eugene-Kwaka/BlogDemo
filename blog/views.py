# I will be able to search across multiple fields
from django.db.models import Q
from django.shortcuts import render, get_object_or_404 ,redirect
from blog.models import *
from blog.forms import *

# Create your views here.

def post_detail(request, category_slug, slug):
    # 'get_object_or_404' is a shortcut to getting a specific post if it doesn't exist error 404 will be displayed
    # 'status=Post.ACTIVE' will only show the posts that are active
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    #CommentForm Logic
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            # this prevents the form from being submitted at first
            comment = form.save(commit=False)
            # This links the comment to the post object defined above
            comment.post = post
            comment.save()
            # after saving the comment the reader will be redirected to the specific post they commented using the slug
            return redirect('post_detail', slug=slug)
        else:
            # If form is not valid it will return an empty form
            form = CommentForm()
    context={'post':post, 'form':form}
    return render(request, 'blog/post_detail.html', context)

#his will lead us to a specific category
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    # This will filter the active posts that exists in the specified category
    posts = category.posts.filter(status=Post.ACTIVE)
    context={'category':category, 'posts':posts}
    return render(request, 'blog/category.html', context)

def search(request):
    query = request.GET.get('query', '')
    # only Active posts are to be shown after search
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query)| Q(intro__icontains=query) |Q(body__icontains=query))
    context={
        'posts':posts, 
        'query':query
    }
    return render(request, 'blog/search_results.html', context)