from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

    title = forms.CharField(error_messages={'required': '제목을 입력하세요.'}, max_length=100, label="제목")
    text = forms.CharField(error_messages={'required': '내용을 입력하세요.'}, widget=forms.Textarea, label="내용")