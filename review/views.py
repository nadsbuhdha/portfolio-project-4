from django.shortcuts import render
from django.views import generic
from .models import AlbumReview
# Create your views here.

class IndexPage(generic.ListView):
    model = AlbumReview
    queryset = AlbumReview.objects.filter(status=1).order_by('-date_created')
    template_name = 'index.html'
    paginate_by = '4'