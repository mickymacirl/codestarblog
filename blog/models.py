from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# Post has a title, slug, author, featured_image, excerpt, updated_on, content, created_on, status,
# and likes
class Post(models.Model):
    # Creating a title field that is a character field with a max length of 200 and is unique.
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # This is creating a field that is a CloudinaryField.
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # This is creating a many to many relationship between the User and the Post.
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

# "The Post class is a Django model, so Django knows that it should be saved in the database."
# 
# Now, let's add a few more things to the Post model:
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """
        The __str__ function is a special function that is called when you use the print function on an
        object
        :return: The title of the question.
        """
        return self.title

    def number_of_likes(self):
        """
        It returns the number of likes associated with a post
        :return: The number of likes for a particular post.
        """
        return self.likes.count()


# Comment is a model that has a post, a name, an email, a body, a created_on date, and an approved
# boolean
class Comment(models.Model):
# Creating a foreign key relationship between the Comment and the Post.
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

# "The Post model has a title, a slug, a body, a publish date, an author, and a list of comments."
# 
# The first thing to notice is that we've imported models from Django. This is how we access the model
# class
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """
        The `__str__` function is a special function that is called when you try to print an object
        :return: The comment body and the name of the person who posted it.
        """
        return f"Comment {self.body} by {self.name}"
