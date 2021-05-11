from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, redirect
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'portal_index.html'

