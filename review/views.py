""" view """

from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import AlbumReview
from .forms import ReviewForm, EditForm, CommentForm


# Create your views here.


class IndexPage(generic.ListView):
    """ homepage """
    model = AlbumReview
    queryset = AlbumReview.objects.filter(status=1, approved=True).order_by(
        "-date_created"
    )
    template_name = "index.html"
    paginate_by = "4"


class ReviewPage(generic.ListView):
    """ review page """
    model = AlbumReview
    queryset = AlbumReview.objects.filter(status=1, approved=True).order_by(
        "-date_created"
    )
    template_name = "reviews.html"
    paginate_by = "8"


class YourPosts(LoginRequiredMixin, generic.ListView):
    """ user can view their own posts """
    model = AlbumReview
    template_name = "your_posts.html"
    paginate_by = "8"

    def get_queryset(self):
        return AlbumReview.objects.filter(author=self.request.user).order_by(
            "-date_created"
        )


class FullReview(View):
    """ full review page """
    def get(self, request, slug, *args, **kwargs):
        """ comments & likes on full review """
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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ post """
        queryset = AlbumReview.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.album_review = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "album_reviews.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class AddPost(SuccessMessageMixin, CreateView):
    """ add post """
    model = AlbumReview
    form_class = ReviewForm
    template_name = "create_post.html"
    success_url = reverse_lazy("home")
    success_message = "Your post was created"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(SuccessMessageMixin, UpdateView):
    """ edit post """
    model = AlbumReview
    form_class = EditForm
    template_name = "edit_post.html"
    success_url = reverse_lazy("home")
    success_message = "Your post was updated"


class DeletePost(SuccessMessageMixin, DeleteView):
    """ delete post """
    model = AlbumReview
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
    success_message = "Your post was deleted"

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)


class LikePost(View):
    """ like a post """
    def post(self, request, slug):
        """ like post """
        post = get_object_or_404(AlbumReview, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("album_reviews", args=[slug]))


def search(request):
    """ search page """
    if request.method == "POST":
        searched = request.POST["searched"]
        reviews = AlbumReview.objects.filter(
            Q(album_title__icontains=searched)
            | Q(artist__icontains=searched, status=1),
            approved=True,
        )
        return render(
            request,
            "search.html",
            {
                "searched": searched,
                "reviews": reviews,
            },
        )
    else:
        return render(request, "search.html", {})
