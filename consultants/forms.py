from django.forms import ModelForm
from .models import Consultant
from django import forms

class ConsultantForm(ModelForm):
  TC = 'Technology Consulting'
  SE = 'Software Engineering'
  D = 'Delivery'
  C = 'Corporate'
  PRACTICE_CHOICES = (
    ('', '--------------------'),
    (TC, 'Technology Consulting'),
    (SE, 'Software Engineering'),
    (D, 'Delivery'),
    (C, 'Corporate'),
  )

  consultant_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  contact_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  practice = forms.ChoiceField(choices=PRACTICE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
  role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  teams = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  skills = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  sectors = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
  class Meta:
    model = Consultant
    fields = '__all__'