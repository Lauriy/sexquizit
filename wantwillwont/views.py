from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


def home_files(request, filename):
    return render(request, filename, {}, content_type='text/plain')
