from django.shortcuts import render, reverse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from bootstrap_modal_forms.generic import (
    BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView,
)

from piloto.app_forms import worker as form
from piloto.app_forms import nomenclators as frm_nomenclators
from security.app_forms import forms as frm_security
from piloto.app_models.workers import Worker, ExternalPerson
from piloto.app_models.science import Thesis
from piloto.app_models.docent import Course, CourseEdition
from django_pdfkit import PDFView


class Index(TemplateView):
    template_name = "piloto_index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        if self.request.user.worker.sex is 'M':
            msg = 'Bienvenido, {}'.format(self.request.user.worker.name)
        else:
            msg = 'Bienvenida, {}'.format(self.request.user.worker.name)

        context.update({'welcome_msg': msg})
        return context


class CreateExternalPerson(BSModalCreateView):
    template_name = 'cruds/create_external_person.html'
    form_class = form.FormExternalPerson
    form_contact = frm_nomenclators.FormContact
    form_user = frm_security.FormUser
    success_message = 'La persona se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:perfil')

    def get_context_data(self, **kwargs):
        context = super(CreateExternalPerson, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.form_class)
        context['form_contact'] = self.form_contact()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form_contact = self.form_contact(request.POST)
        form.request = request

        if form.is_valid() and form_contact.is_valid():
            contact = form_contact.save()
            external_person = form.save(commit=False)
            external_person.contact = contact
            external_person.save()

            if request.is_ajax():
                data = {
                    'title': "Notificación",
                    'message': self.success_message,
                }
                return JsonResponse(data)
            else:
                pass
        else:
            return super(CreateExternalPerson, self).post(request, *args, **kwargs)

"""
class CV(PDFView):
    template_name = "cv.html"
    form_class = frm_piloto.FormPerfilpiloto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['piloto'] = self.request.user.piloto        
        return context

class Modificarpiloto(BSModalUpdateView):
    model = piloto
    template_name = 'modificar_datos_personales.html'
    form_class = frm_piloto.FormModificarDatosPersonales
    success_message = 'Sus datos personales fueron modificados satisfactoriamente.'
    success_url = reverse_lazy('piloto:perfil')

    def form_valid(self, form):
        response = super(Modificarpiloto, self).form_valid(form)

        if self.request.is_ajax():     
            if form.is_valid():
                f = form.save(commit=False)
                f.save()
                datos = {
                    'title': "Notificación",
                    'message': self.success_message,
                    #'data': form.cleaned_data,
                }
            return JsonResponse(datos)
        else:
            return response
"""



