""" urls """
from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexPage.as_view(), name="home"),
    path("reviews/", views.ReviewPage.as_view(), name="review_page"),
    path("create_post/", views.AddPost.as_view(), name="add_post"),
    path("search/", views.search, name="search"),
    path("your_posts/", views.YourPosts.as_view(), name="your_posts"),
    path("edit_post/<slug:slug>", views.EditPost.as_view(), name="edit_post"),
    path("delete_post/<slug:slug>", views.DeletePost.as_view(),
         name="delete_post"),
    path("<slug:slug>/", views.FullReview.as_view(), name="album_reviews"),
    path("like/<slug:slug>", views.LikePost.as_view(), name="post_like"),
]
