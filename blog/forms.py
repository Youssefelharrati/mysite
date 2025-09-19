from django.forms import ModelForm
from .models import Post, Comment
from django import forms
 
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'title', 'text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-texterea postcontent'})
        }

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-texterea'})
        }