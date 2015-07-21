from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'text', 'date', 'is_posted', 'slug']}),
    ]
    prepopulated_fields = {
        'slug': ('title',),
    }

admin.site.register(Post, PostAdmin)