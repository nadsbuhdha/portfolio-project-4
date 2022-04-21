from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from .models import AlbumReview
# Create your views here.

class IndexPage(generic.ListView):
    model = AlbumReview
    queryset = AlbumReview.objects.filter(status=1).order_by('-date_created')
    template_name = 'index.html'
    paginate_by = '4'


class ReviewPage(generic.ListView):
    model = AlbumReview
    queryset = AlbumReview.objects.filter(status=1).order_by('-date_created')
    template_name = 'reviews.html'
    paginate_by = '8'


class FullReview(View):
   def get(self, request, slug, *args, **kwargs):
        queryset = AlbumReview.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "album_reviews.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )


class AddPost(CreateView):
    model = AlbumReview
    template_name = 'create_post.html'
    fields = ['album_title', 'artist', 'genre', 
    'album_image', 'album_score', 'body', 'status']
