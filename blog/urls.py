# Importing the views.py file from the current directory and importing the path function from the
# django.urls module.
from . import views
from django.urls import path

# A list of url patterns.
urlpatterns = [
    # This is a url pattern that matches a url with an empty string.
    path('', views.PostList.as_view(), name='home'),
    # This is a url pattern that matches a url with a slug.
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
