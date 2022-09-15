from dataclasses import field
from django import forms
from . models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'content', 'image', 'published_date']
        widgets = {'title': forms.TextInput(
            attrs={'class': 'form-control'}), 'author': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'published_date': forms.DateTimeInput(attrs={'class': 'form-control'})}
