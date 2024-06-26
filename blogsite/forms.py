from .models import CommentOn, Contact
from django import forms
from django.forms import ModelForm


class CommentOnForm(forms.ModelForm):
    class Meta:
        model = CommentOn
        fields = ('body',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'about']
