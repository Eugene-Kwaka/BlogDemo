from django.contrib import admin
from blog.models import *

class CommentItemInline(admin.TabularInline):
    model = Comment
    row_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    # prepopulates the slug fields
    prepopulated_fields = {'slug':('title',)}
    # the comments will be shown in the posts
    inlines = (CommentItemInline,)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'post', 'created_at']


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)