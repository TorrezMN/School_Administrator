from django.shortcuts import render
from django.views.generic import TemplateView



class Admin_Home(TemplateView):
    template_name = 'admin_home.html'