from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comments
from .models import Post

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment',]
        exclude = ['commentor', 'post']
        
        
        
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','description','title', 'link']
        exlude =  ['author','date_posted']