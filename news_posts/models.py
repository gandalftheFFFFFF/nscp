from django.db import models

# Create your models here.

class Post(models.Model):
    """
    This class is used to post news to the site.
    """

    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()
    is_posted = models.BooleanField(default=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']