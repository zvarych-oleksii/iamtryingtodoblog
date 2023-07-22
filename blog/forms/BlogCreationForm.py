from django import forms
from ..models import Post_written

class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Post_written
        fields = ['title', 'content', 'category', 'image']


class FileForm(forms.Form):
    file = forms.FileField()

