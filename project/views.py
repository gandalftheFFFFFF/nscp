from django.shortcuts import render, get_object_or_404
import calendar
from .models import Project

# Create your views here.


def projects(request):
    template = 'projects.html'
    try:
        projects = Project.objects.all()[:2]
    except Project.DoesNotExist:
        projects = None
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


def projects_archive(request):
    template = 'projects_archive.html'
    try:
        projects = Project.objects.all()
    except Project.DoesNotExist:
        projects = None

    if projects:
        archive = {}
        for project in projects:
            month = calendar.month_name[project.date_added.month]
            if month in archive:
                archive[month].append(project)
            else:
                archive[month] = [project,]

    context = {
        'archive':archive,
    }
    return render(request, template, context)