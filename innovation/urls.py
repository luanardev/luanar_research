from django.urls import path
from . import views
from .views import ( InnovationsView, InnovationDetails)

urlpatterns = [
    
    path('innovations/', InnovationsView.as_view(), name='innovations'),
    path('innovation_details/<uuid:pk>/', InnovationDetails.as_view(), name='innovation_details'),
]
