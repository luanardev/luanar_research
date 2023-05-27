from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import Subscription
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
import uuid
from .forms import SubscriptionForm

# Create your views here.


def subscribe(request):
    form = SubscriptionForm()
    if request.method == 'POST' :
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form }
    return render(request, 'subscription/form.html', context)
    # if request.method == 'POST':
    #     form = SubscriptionForm(request.POST)
    #     if form.is_valid:
    #         form.save()

    
    # form = SubscriptionForm(request)
    # if(form.is_valid):
    #     form.save()

    # return redirect('index')

def test_mail(request):
    send_mail(
    'Appeals System',
    'Guys, osayiwala kumaliza system ya a DVC. Osafooka!',
    'saris@luanar.ac.mw',
    ["noelng'ona@luanar.ac.mw", "jkambere@luanar.ac.mw", "bngwira@luanar.ac.mw", "bsimpokolwe@luanar.ac.mw", "ezembeni@luanar.ac.mw"],
)
    return redirect('index')



           