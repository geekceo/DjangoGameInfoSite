from django import forms
from .models import *

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'game']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'comment-area', 'cols': 90, 'rows': 5})
        }

