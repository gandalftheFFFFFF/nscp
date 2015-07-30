from django.db import models

# Create your models here.

RELATED_TO_CHOICES = (('school', 'School'),
                       ('private', 'Private'),
                       ('work', 'Work'))

class Project(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    git_url = models.URLField()
    description = models.TextField()
    related_to = models.CharField(max_length=200, choices=RELATED_TO_CHOICES)
    date_added = models.DateField()
    slug = models.SlugField()

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name
