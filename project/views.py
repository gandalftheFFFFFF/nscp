from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project
# Create your views here.

def projects(request):
    template = 'projects.html'
    projects = get_list_or_404(Project)
    context = {
        'projects':projects
    }
    return render(request, template, context)


def specific_project(request, project_slug):
    template = 'specific_project.html'
    project = get_object_or_404(Project, slug=project_slug)
    context = {
        'project':project
    }
    return render(request, template, context)