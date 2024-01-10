from .models import TestModel,AddPHoto
from django.shortcuts import render
from django import forms

class PhotoForm(forms.ModelForm):
    class Meta:
        model=AddPHoto
        fields="__all__"