from . import views
from django.urls import path

urlpatterns = [
    path("", views.IndexPage.as_view(), name="home"),
    path("reviews/", views.ReviewPage.as_view(), name="review_page"),
    path("<slug:slug>/", views.FullReview.as_view(), name="album_reviews")
]