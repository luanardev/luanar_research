from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import InnovationSerializer
from .models import  Innovation
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
import uuid



# Create your views here.


class InnovationsView(ListView):
    template_name = 'core/innovations.html'
    model = Innovation
    paginate_by = 3
    def get_context_data(self,*args, **kwargs):
        context = super(InnovationsView, self).get_context_data(*args,**kwargs)
        context['page_name'] = 'Innovations'
        return context

class InnovationDetails(DetailView):
    template_name = 'core/innovation_details.html'
    context_object_name = 'innovation'
    queryset = Innovation.objects.all()