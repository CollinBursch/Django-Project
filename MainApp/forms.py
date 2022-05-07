from django import forms

from .models import Comment 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['pizza']
        labels = {'pizza':'', 'commentor_name':'', 'comment_text':''}
        