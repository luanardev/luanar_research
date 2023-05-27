from django.forms  import ModelForm
from .models import Subscription
from django import forms

class SubscriptionForm(ModelForm):
    error_css_class = "error"
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class" : "form-control"}))
    class Meta:
        model = Subscription
        fields = '__all__'


