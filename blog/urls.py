from django.urls import path
from blog.views import *

urlpatterns=[
    path('search/', search, name="search"),
    # 'slug' will be the identifier for the specific post in the url
    path('<slug:category_slug>/<slug:slug>/', post_detail, name="post_detail"),  
    path('<slug:slug>/', category, name='category'),
]