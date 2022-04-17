from django.contrib import admin
from .models import AlbumReview, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(AlbumReview)
class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
    prepopulated_fields = {'slug': ('album_title',)}
    list_filter = ('date_created', 'status')
    list_display = ('album_title', 'slug', 'status', 'date_created')
    search_fields = ['album_title', 'artist']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This class defines the appearance and control over the comments in
    the admin.
    """
    list_display = ('name', 'comment_body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'comment_body']
    actions = ['approve_comments'] 

    def approve_comments(self, request, queryset):
        """
        approval of comments
        """
        queryset.update(approved=True)

