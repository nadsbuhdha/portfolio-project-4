from . import views
from django.urls import path

urlpatterns = [
    path("", views.IndexPage.as_view(), name="home"),
    path("reviews/", views.ReviewPage.as_view(), name="review_page"),
    path("create_post/", views.AddPost.as_view(), name="add_post"),
    path("<slug:slug>/", views.FullReview.as_view(), name="album_reviews"),
]