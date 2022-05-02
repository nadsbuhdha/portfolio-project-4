from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from slugger import AutoSlugField
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class AlbumReview(models.Model):
    album_title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='album_title', unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='review_likes', blank=True)
    album_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_auth')
    album_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)]) # noqa
    approved = models.BooleanField(default=False)
    body = models.TextField(default='Add your review here')
    
    

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
         return self.album_title
        
    def num_of_likes(self):
       return self.likes.count()
    
    def get_absolute_url(self):
        return reverse("album_reviews", kwargs={"slug": self.slug})
    
    
    

class Comment (models.Model):
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment_body} by {self.name}"