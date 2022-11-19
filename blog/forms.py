# Importing the Comment model from the models.py file in the same directory.
from .models import Comment
from django import forms


# "The CommentForm class is a ModelForm that will be used to create and update Comment objects."
# 
# The Meta class tells Django which model should be used to create this form (model = Comment)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
