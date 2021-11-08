from django import forms

from .models import Comments, Post, PostImages

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text',)

class ImageForm(forms.ModelForm):
    title=forms.TextInput()
    image = forms.ImageField(label='Image')    
    class Meta:
        model = PostImages
        fields = ('image', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("text", )