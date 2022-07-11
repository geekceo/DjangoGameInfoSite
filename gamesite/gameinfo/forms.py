from django import forms
from .models import *

class AddCommentForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'comment-area', 'cols': 90, 'rows': 5}))