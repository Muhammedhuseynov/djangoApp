from django import forms
from .models import Post, Comm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]
        labels = {
            'title':'Ady:',
            'content':'Waka:'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comm
        fields = ['comment']