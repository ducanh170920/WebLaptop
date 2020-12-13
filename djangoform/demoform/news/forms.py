from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)

class SendEmail(forms.Form):
    title = forms.CharField(max_length=200)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

