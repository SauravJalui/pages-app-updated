from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    '''This class contains the data to be displayed on the home page'''
    template_name = 'home.html'

class AboutPageView(TemplateView):
    '''This class contains the data to be displayed on the about page'''
    template_name = 'about.html'