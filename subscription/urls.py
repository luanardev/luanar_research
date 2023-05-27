from django.urls import path
from . import views
# from .views import (
#     Collections,CollectionDetails,IndexView,
#     PublicationsView,PublicationDetails, LicenseView, PublicationTypeView)

urlpatterns = [
    path('subscribe', views.subscribe, name='subscribe'),
    path('test', views.test_mail, name='test_mail'),
    
]
