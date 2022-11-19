# Importing the admin module from Django, the Post and Comment models from the current directory,
# and the SummernoteModelAdmin class from the django_summernote.admin module.
from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# A decorator that registers the Post model with the admin site.
@admin.register(Post)
# A class that is used to create a post.

class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# A decorator that registers the Comment model with the admin site.
@admin.register(Comment)
# The CommentAdmin class inherits from the ModelAdmin class, and defines a list_display, list_filter,
# search_fields, and actions
class CommentAdmin(admin.ModelAdmin):
    # A list of fields that will be displayed on the change list page of the admin.
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    # A list of fields by which you can filter the change list.
    list_filter = ('approved', 'created_on')
    # A list of fields that will be searched whenever somebody submits a search query in that text
    # field in the upper-right corner of the change list page.
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
