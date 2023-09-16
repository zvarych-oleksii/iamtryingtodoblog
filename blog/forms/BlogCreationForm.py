from django import forms
from ..models import posts 

class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = posts.Post_written
        fields = ['title', 'content', 'category', 'image']


class FileForm(forms.Form):
    file = forms.FileField()

