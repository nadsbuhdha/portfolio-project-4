from django.contrib import admin
from .models import AlbumReview
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(AlbumReview)
class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')

# admin.site.register(AlbumReview)
