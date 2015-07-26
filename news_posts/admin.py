from django.contrib import admin
from .models import Post
from ImageUploader.models import Image
# Register your models here.

class ImagesInline(admin.StackedInline):
    model = Image
    extra = 0

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'text', 'date', 'is_posted', 'slug']}),
    ]
    inlines = [ImagesInline]
    prepopulated_fields = {
        'slug': ('title',),
    }

admin.site.register(Post, PostAdmin)