from django.urls import path
from . import views
from .views import ( InnovationsView, InnovationDetails)

urlpatterns = [
    
    path('', InnovationsView.as_view(), name='innovations'),
    path('innovation-details/<uuid:pk>', InnovationDetails.as_view(), name='innovation-details'),

    
]
