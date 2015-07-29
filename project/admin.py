from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name',
                           'url',
                           'git_url',
                           'description',
                           'related_to',
                           'slug',
                           ]}),
    ]

    prepopulated_fields = {
        'slug': ('name',),
    }

admin.site.register(Project, ProjectAdmin)