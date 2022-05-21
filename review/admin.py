""" admin """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import AlbumReview, Comment


@admin.register(AlbumReview)
class ReviewAdmin(SummernoteModelAdmin):
    """ review page admin """

    summernote_fields = "body"
    prepopulated_fields = {"slug": ("album_title",)}
    list_filter = ("date_created", "status")
    list_display = ("album_title", "slug", "status", "date_created")
    search_fields = ["album_title", "artist"]
    actions = ["approve_reviews", "disapprove_reviews"]

    def approve_reviews(self, request, queryset):
        """
        approval of reviews
        """
        queryset.update(approved=True)

    def disapprove_reviews(self, request, queryset):
        """
        dissapprove of reviews
        """
        queryset.update(approved=False)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    comment control
    """

    list_display = ("name", "comment_body", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ["name", "email", "comment_body"]
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        """
        approval of comments
        """
        queryset.update(approved=True)
