from django import forms

from .models import Comment 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['pizza', 'commentor_name', 'comment_text']
        labels = {'pizza':'Pizza Name', 'commentor_name':'Username', 'comment_text':'Comment'}
        