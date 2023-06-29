from django.shortcuts import render
from .models import Project
from django.views.generic import ListView, DetailView

# Create your views here.
class ProjectsView(ListView):
    template_name = 'core/projects.html'
    model = Project
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_approved=True)
        return queryset

class ProjectDetails(DetailView):
    template_name = 'core/project_details.html'
    context_object_name = 'project'
    queryset   = Project.objects.all()