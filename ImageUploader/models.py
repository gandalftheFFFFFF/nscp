from django.db import models
from news_posts.models import Post
# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images')
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.name