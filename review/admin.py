from django.contrib import admin
from .models import AlbumReview
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(AlbumReview)
class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
    prepopulated_fields = {'slug': ('album_title',)}
    list_filter = ('date_created', 'status')
    list_display = ('album_title', 'slug', 'status', 'date_created')
    search_fields = ['album_title', 'artist']
    

# admin.site.register(AlbumReview)
