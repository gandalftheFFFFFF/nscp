# NSCP
This is my personal website written in Django. It is also my second ever project in django.
The project is a simple website that serves as a showcase of me and my work. The site has a 
simple blog system that I use to post news about events and new projects, and a system where
I can present my projects in a uniform way.

## Contents

### Blog app
The blog app is located in the folder *news_posts* and is called as such. It has a very simple model:

    class Post(models.Model):
        title = models.CharField(max_length=200)
        text = models.TextField()
        date = models.DateTimeField()
        is_posted = models.BooleanField(default=True)
        slug = models.SlugField()

It is also possible to add images to a blog post.

### Projects app
The projects app os in the folder *project* and also has a simple model:

    class Project(models.Model):
        name = models.CharField(max_length=200)
        url = models.URLField()
        git_url = models.URLField()
        description = models.TextField()
        related_to = models.CharField(max_length=200, choices=RELATED_TO_CHOICES)
        date_added = models.DateField()
        slug = models.SlugField()

Where `RELATED_TO_CHOICES` is a list of strings like 'private', 'work', 'school', etc.


# TODO:

- Improve news archive to include search bar
- Insert new 'category' field for projects; java, python, django, scala, etc
- Add a 'preview' section to the site, to be able to preview smaller apps/projects
- Include Dojo rich text editor in blog app


