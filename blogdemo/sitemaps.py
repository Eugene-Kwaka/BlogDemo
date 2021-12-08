from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import Category, Post 

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)

    # This displays last modified date for the post
    def lastmod(self, obj):
        return obj.created_at