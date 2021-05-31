from django import forms
from .models import Post, Answer

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }

        labels = {
            'title': '제목',
            'text': '내용'
        }

    #title = forms.CharField(error_messages={'required': '제목을 입력하세요.'}, max_length=100, label="제목")
    #text = forms.CharField(error_messages={'required': '내용을 입력하세요.'}, widget=forms.Textarea, label="내용")


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('number', 'text',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }

        labels = {
            'number': '글 번호',
            'text': '답변'
        }
    # text = forms.CharField(error_messages={'required': '답변하세요.'}, widget=forms.Textarea, label="답변")