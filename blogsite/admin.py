from django.contrib import admin
from .models import Post, CommentOn
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

# Register your models here.