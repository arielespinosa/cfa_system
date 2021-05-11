from django.forms.models import model_to_dict
from django.http import  JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from cfa_system.mixins.mixins_views import SingleCreateObjectMixin
from piloto.app_models.nomenclators import *
from piloto.app_forms import nomenclators as forms
from piloto.app_forms import inventory as frm_inventory


class CreateCertificationView(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_certification.html'
    form_class = forms.FormCertification
    success_message = 'La certificación se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreatePrizeView(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_prize.html'
    form_class = forms.FormPrize
    success_message = 'El premio se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreateEntity(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_entity.html'
    form_class = forms.FormEntity
    success_message = 'La entidad se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreateStudyCenter(SingleCreateObjectMixin, BSModalCreateView):
    form_class = forms.FormStudyCenter
    template_name = 'cruds/nomenclators/create_study_center.html'
    success_message = 'El centro se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreateProgram(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_program.html'
    form_class = forms.FormProgram
    success_message = 'El programa se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreateClient(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_client.html'
    form_class = forms.FormClient
    success_message = 'El Cliente se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreateCostCenter(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_cost_center.html'
    form_class = forms.FormCostCenter
    success_message = 'El Centro de Costo se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreateKnowledgeField(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_knowledge_field.html'
    form_class = forms.FormKnowledgeField
    success_message = 'La Especialidad se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreateField(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_field.html'
    form_class = forms.FormField
    success_message = 'La Especialidad se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreateOccupation(BSModalCreateView):
    template_name = 'cruds/nomenclators/create_occupation.html'
    form_class = forms.FormOccupation
    success_message = 'La Especialidad se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreateOffice(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_office.html'
    form_class = forms.FormOffice
    success_message = 'La Especialidad se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreatePeopleOrganism(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_people_organism.html'
    form_class = forms.FormPeopleOrganism
    success_message = 'La Especialidad se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreatePoliticOrganism(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_politic_organism.html'
    form_class = forms.FormPoliticOrganism
    success_message = 'La Especialidad se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreateTask(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_task.html'
    form_class = forms.FormTask
    success_message = 'La tarea se creo satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class CreateEvent(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/nomenclators/create_event.html'
    form_class = forms.FormEvent
    success_message = 'La tarea se creo satisfactoriamente.'
    success_url = reverse_lazy('piloto:science_work')


"""
class ViewCertifications(BSModalReadView):
    model = Certification
    template_name = 'crud/view_certification.html'


class DeleteCertification(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Certification
    template_name = 'eliminar_elemento.html'
    success_message = 'La certification fue eliminada de su CV satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class ListaCertificationes(ListView):
    template_name = 'crud/listar_Certificationes.html'

    def get_queryset(self):
        return Certification.objects.order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(ListaCertificationes, self).get_context_data(**kwargs)
        context.update({
            'Certificationes': self.get_queryset,
        })
        return context


class ViewCentroEstudios(BSModalReadView):
    model = CentroEstudios
    template_name = 'crud/View_centro_de_estudios.html'
"""
"""

class DeleteCentroEstudios(BSModalAjaxFormMixin, BSModalDeleteView):
    model = CentroEstudios
    template_name = 'Delete_elemento.html'
    success_message = 'El centro fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')


class ListaCentrosEstudios(ListView):
    template_name = 'centros_de_estudios.html'

    def get_queryset(self):
        return CentroEstudios.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListaCentroEstudios, self).get_context_data(**kwargs)
        context.update({
            'eventos': self.get_queryset,
        })
        return context

class CreateContact(BSModalCreateView):
    template_name = 'crud/create_contact.html'
    form_class = frm_piloto.FormCreateContact
    success_message = 'El contacto se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')

    def get_context_data(self, **kwargs):
        context = super(CreateContact, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'Contact': {},
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            Contact = form.save()
            Contact.save()

            data.update({
                'Contact': model_to_dict(Contact),
            })
            return JsonResponse(data)
        else:
            return super(CreateContact, self).post(request, *args, **kwargs)


class CreateAreaInteres(BSModalCreateView):
    template_name = 'crud/Create_area_de_interes.html'
    form_class = frm_piloto.FormCreateAreaInteres
    success_message = 'El area de interes se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')

    def get_context_data(self, **kwargs):
        context = super(CreateAreaInteres, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'area_de_interes': {},
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            area_de_interes = form.save()
            area_de_interes.save()

            data.update({
                'area_de_interes': model_to_dict(area_de_interes),
            })
            return JsonResponse(data)
        else:
            return super(CreateAreaInteres, self).post(request, *args, **kwargs)


class CreateMunicipio(BSModalCreateView):
    template_name = 'crud/Create_municipio.html'
    form_class = frm_piloto.FormCreateMunicipio
    success_message = 'El municipio se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')

    def get_context_data(self, **kwargs):
        context = super(CreateMunicipio, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'Municipio': {},
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            municipio = form.save()
            municipio.save()

            data.update({
                'municipio': model_to_dict(municipio),
            })
            return JsonResponse(data)
        else:
            return super(CreateMunicipio, self).post(request, *args, **kwargs)
"""




