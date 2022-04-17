from . import views
from django.urls import path

urlpatterns = [
    path("", views.IndexPage.as_view(), name="index"),
    path("reviews/", views.ReviewPage.as_view(), name="review_page"),
]