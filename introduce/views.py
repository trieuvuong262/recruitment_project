from django.shortcuts import render
from .models import CompanyIntroduction

def get_introduction():
    return CompanyIntroduction.objects.first()
