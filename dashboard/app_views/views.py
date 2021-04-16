from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from dashboard.app_models.models import App


class Index(TemplateView):
    template_name = 'dashboard_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['apps'] = App.objects.all()

        return context


class OpenApp(TemplateView):

    def get(self, request, *args, **kwargs):
        return redirect('{}:index'.format('a'))




