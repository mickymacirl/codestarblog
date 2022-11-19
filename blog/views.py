# Importing the Post model from the models.py file.
from django.shortcuts import render, get_object_or_404 
from django.views import generic, View
from .models import Post

# List view of Post objects, and use the template index.html to render
# them.
# 
# The model attribute tells Django which model should be used to create this view. In this case,
# using the Post model
class PostList(generic.ListView):
    model = Post
    # This is a queryset that filters the Post objects by status and orders them by created_on.
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # Paginate the results and split them to 6 objects per page.
    paginate_by = 6

# We're creating a class called PostDetail that inherits from the View class. 
# 
# The get method is called when a GET request is made to the server. 
# 
# The get method takes in a request object, which contains information about the request that was made
# to the server. 
# 
# The get method also takes in a slug, which is the unique identifier for a post. 
# 
# The get method then returns a response object, which contains information about the response that
# the server will send back to the client. 
# 
# The get method is responsible for rendering the post_detail.html template. 
# 
# The post_detail.html template is rendered with the post, comments, and liked variables. 
# 
# The post variable is a Post object that contains information about the post that was requested. 
# 
# The comments variable is a list of Comment objects that contain information about the comments that
# were made on the post.
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # Filtering the Post objects by status and orders them by created_on.
        queryset = Post.objects.filter(status=1)
        # Getting the Post object that has the slug that was passed in.
        post = get_object_or_404(queryset, slug=slug)
        # This is a queryset that filters the Comment objects by approved and orders them by
        # created_on.
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        # This is checking if the user has liked the post. If they have, then the liked variable is
        # set to True.
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Rendering the post_detail.html template with the post, comments, and liked variables.
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )