from django import forms 
from .models import AlbumReview, Comment
from django_summernote.widgets import SummernoteInplaceWidget, SummernoteWidget

class ReviewForm(forms.ModelForm):
    class Meta:
        model = AlbumReview
        fields = ('album_title', 'artist', 'genre', 
        'album_image', 'album_score', 'body', 'status')
        
        
        widgets = {
        'album_title': forms.TextInput(attrs={'class': 'form-control'}),
        'album_score': forms.NumberInput(attrs={'class': 'form-control'}),
        'genre': forms.TextInput(attrs={'class': 'form-control'}),
        'artist': forms.TextInput(attrs={'class': 'form-control'}),
        'status': forms.Select(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
        'album_image': forms.FileInput(attrs={'class': 'form-control'}),
    }
    

class EditForm(forms.ModelForm):
    class Meta:
        model = AlbumReview
        fields = ('album_title', 'artist', 'genre', 
        'album_image', 'album_score', 'body', 'status')
        
        
        widgets = {
        'album_title': forms.TextInput(attrs={'class': 'form-control'}),
        'album_score': forms.NumberInput(attrs={'class': 'form-control'}),
        'genre': forms.TextInput(attrs={'class': 'form-control'}),
        'artist': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
        'status': forms.Select(attrs={'class': 'form-control'}),
        'album_image': forms.FileInput(attrs={'class': 'form-control'}),
    }
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
