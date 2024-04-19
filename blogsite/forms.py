from .models import CommentOn
from django import forms

class CommentOnForm(forms.ModelForm):
    class Meta:
        model = CommentOn
        fields = ('body',)