# Django model for blog post and users authentication
from django.db import models
from django.contrib.auth.models import User

status = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) # title of the post
    slug = models.SlugField(max_length=200, unique=True) # slug (friendly URL) for the post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # author of the post via foreign key
    updated_on = models.DateTimeField(auto_now=True) # last updated date
    content = models.TextField() # content of the post
    created_on = models.DateTimeField(auto_now_add=True) # created date
    status = models.IntegerField(choices=status, default=0) # status of the post

    class Meta: # meta class for ordering the posts by created date
        ordering = ['-created_on'] # order by created date


    def __str__(self): # string representation of the post
        return self.title # return the title of the post

    def get_absolute_url(self): # get the absolute URL of the post
        from django.urls import reverse # import reverse function from django.urls
        return reverse("post_detail", kwargs={"slug": str(self.slug)}) # return the URL of the post

