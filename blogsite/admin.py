from django.contrib import admin
from .models import Post, CommentOn, Contact
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class AdminPost(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created')
    list_display = ('title', 'slug', 'status', 'created',)
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(CommentOn)
class AdminComment(admin.ModelAdmin):
    list_filter = ('created', 'approved')
    list_display = ('name', 'body', 'post', 'created', 'approved')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Contact)
