""" forms """
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import AlbumReview, Comment


class ReviewForm(forms.ModelForm):
    """ review form """
    class Meta:
        """ fields on form """
        model = AlbumReview
        fields = (
            "album_title",
            "artist",
            "genre",
            "album_image",
            "album_score",
            "body",
            "status",
        )

        widgets = {
            "album_title": forms.TextInput(attrs={"class": "form-control"}),
            "album_score": forms.NumberInput(attrs={"class": "form-control"}),
            "genre": forms.TextInput(attrs={"class": "form-control"}),
            "artist": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "body": SummernoteWidget(),
            "album_image": forms.FileInput(attrs={"class": "form-control"}),
        }


class EditForm(forms.ModelForm):
    """ edit form """
    class Meta:
        """ fields on form """
        model = AlbumReview
        fields = (
            "album_title",
            "artist",
            "genre",
            "album_image",
            "album_score",
            "body",
            "status",
        )

        widgets = {
            "album_title": forms.TextInput(attrs={"class": "form-control"}),
            "album_score": forms.NumberInput(attrs={"class": "form-control"}),
            "genre": forms.TextInput(attrs={"class": "form-control"}),
            "artist": forms.TextInput(attrs={"class": "form-control"}),
            "body": SummernoteWidget(),
            "status": forms.Select(attrs={"class": "form-control"}),
            "album_image": forms.FileInput(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    """ comment form """
    class Meta:
        """ fields on form """
        model = Comment
        fields = ("comment_body",)
