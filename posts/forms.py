from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Post Title',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Share you experience here...',
            })
        }