from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, redirect
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from cfa_system.mixins.mixins_views import SingleCreateObjectMixin
from piloto.app_models.docent import *
from piloto.app_models.science import Thesis, Result, Project, Article
from piloto.app_forms import docent as forms


# CREATE VIEWS
class CreateCourse(SingleCreateObjectMixin, generic.CreateView):
    template_name = 'cruds/docent/create_course.html'
    form_class = forms.FormCourse
    success_message = 'El curso se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:create_course_edition')


class CreateCourseEdition(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/docent/create_course_edition.html'
    form_class = forms.FormCourseEdition
    success_message = 'El curso se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:course_editions')

    def post(self, request, *args, **kwargs):
        """
        # Añadir los cursos seleccionados al Worker
        cursos_realizados = request.POST.getlist('cursos')
        if cursos_realizados:
            for course_edition_pk in cursos_realizados:
                curso = CourseEdition.objects.get(pk=course_edition_pk)
                curso.students.add(request.user.Worker)
                # data['cursos'].update(model_to_dict(curso))
        """

        form_course_edition = self.get_form(self.form_class)
        form_course_edition.request = request

        if form_course_edition.is_valid():
            teacher_pk = request.POST.get('teacher')

            try:
                teacher = Worker.objects.get(pk=teacher_pk)
            except ObjectDoesNotExist:
                teacher = ExternalPerson.objects.get(pk=teacher_pk)

            course_edition = form_course_edition.save(commit=False)
            course_edition.edition = CourseEdition.objects.filter(course__pk=course_edition.course.pk).count() + 1
            course_edition.teacher = teacher
            course_edition.save()
            form_course_edition.save_m2m()

            return HttpResponseRedirect(self.success_url)
        else:
            return super(CreateCourseEdition, self).post(request, *args, **kwargs)


class CreateTribunal(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/docent/create_tribunal.html'
    form_class = forms.FormTribunal
    success_message = 'El tribunal se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:tribunals')

    def post(self, request, *args, **kwargs):
        form_tribunal = self.get_form(self.form_class)
        form_tribunal.request = request

        if form_tribunal.is_valid():
            tribunal = form_tribunal.save(commit=False)
            tribunal.save()

            # Añadir los students de tribunal
            members = request.POST.getlist('members')
            for member_pk in members:
                try:
                    member = Worker.objects.get(pk=member_pk)
                except ObjectDoesNotExist:
                    member = ExternalPerson.objects.get(pk=member_pk)
                tribunal.members.add(member)
            tribunal.members.add(request.user.worker)

            return HttpResponseRedirect(self.success_url)
        else:
            return super(CreateTribunal, self).post(request, *args, **kwargs)


class CreateOponency(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/docent/create_oponency.html'
    form_class = forms.FormOponency
    success_message = 'La oponencia se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:oponencys')

    def post(self, request, *args, **kwargs):
        """
        oponencys = request.POST.getlist('Oponencys')
        if Oponencys:
            for Oponency_pk in Oponencys:
                Oponency = Oponency.objects.get(pk=Oponency_pk)
                request.user.Worker.Oponencys.add(Oponency)
                # data['Oponencys'].update(model_to_dict(Oponency))
        """
      
        form_oponency = self.get_form(self.form_class)
        form_oponency.request = request
  
        if form_oponency.is_valid():
            element_pk = request.POST.get('element')

            try:
                element = Article.objects.get(pk=element_pk)
            except ObjectDoesNotExist:
                pass
            try:
                element = Thesis.objects.get(pk=element_pk)
            except ObjectDoesNotExist:
                pass
            try :
                element = Result.objects.get(pk=element_pk)
            except ObjectDoesNotExist:
                pass
            try:
                element = Project.objects.get(pk=element_pk)
            except ObjectDoesNotExist:
                pass

            oponency = form_oponency.save(commit=False)
            oponency.element = element
            oponency.save()

            opponents_pk = request.POST.getlist('opponents')
            for pk in opponents_pk:
                try:
                    opponent = Worker.objects.get(pk=pk)
                except ObjectDoesNotExist:
                    opponent = ExternalPerson.objects.get(pk=pk)
                oponency.opponents.add(opponent)
            oponency.opponents.add(request.user.worker)

            return HttpResponseRedirect(self.success_url)
        else:
            return super(CreateOponency, self).post(request, *args, **kwargs)


class CreateWorkerCertification(SingleCreateObjectMixin, BSModalCreateView):
    template_name = 'cruds/docent/create_worker_certification.html'
    form_class = forms.FormWorkerCertification
    success_message = 'El certificado se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:worker_certifications')

    def post(self, request, *args, **kwargs):
        form_certification = self.get_form(self.form_class)
        form_certification.request = request

        if form_certification.is_valid():
            worker_certification = form_certification.save(commit=False)
            worker_certification.worker = request.user.worker
            worker_certification.save()

            return HttpResponseRedirect(self.success_url)
        else:
            return super(CreateWorkerCertification, self).post(request, *args, **kwargs)


# LIST VIEWS
class ListCourse(generic.ListView):
    template_name = 'cruds/docent/courses.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super(ListCourse, self).get_context_data(**kwargs)
        return context


class ListCourseEdition(generic.ListView):
    template_name = 'cruds/docent/courses.html'
    model = CourseEdition

    def get_queryset(self):
        if 'worker_pk' in self.kwargs.keys():
            worker = Worker.objects.get(pk=int(self.kwargs.keys('worker_pk')))
            return worker.courses
        else:
            return super(ListCourseEdition, self).get_queryset()

    def tbl_ajax_content(self):
        data = []

        for course in self.request.user.worker.courses.all():
            checkbox = """
                 <td>
                   <label class='mt-checkbox mt-checkbox-single mt-checkbox-outline'>
                       <input type='checkbox' class='checkboxes' value='{}' />
                       <span></span>
                   </label>
                 </td>
             """.format(course.pk)
            data.append([checkbox, course.name, course.display_edition(), course.teacher.coloquial_name, course.start_date, ''])
        return data

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse({"data": self.tbl_ajax_content()})
        else:
            return super(ListCourseEdition, self).get(request, *args, **kwargs)


class ListTribunal(generic.ListView):
    template_name = 'cruds/docent/tribunals.html'
    model = Tribunal

    def get_context_data(self, **kwargs):
        context = super(ListTribunal, self).get_context_data(**kwargs)

        tribunals_paginator = Paginator(self.request.user.worker.tribunals.all(), 15)
        tribunals_page = self.request.GET.get('pag')
        if tribunals_paginator.count > 0:
            context['tribunals'] = tribunals_paginator.get_page(tribunals_page)

        return context


class ListOponency(generic.ListView):
    template_name = 'cruds/docent/oponencys.html'
    model = Oponency

    def get_context_data(self, **kwargs):
        context = super(ListOponency, self).get_context_data(**kwargs)

        oponencys_paginator = Paginator(self.request.user.worker.oponencys.all(), 15)
        oponencys_page = self.request.GET.get('pag')
        if oponencys_paginator.count > 0:
            context['oponencys'] = oponencys_paginator.get_page(oponencys_page)

        return context


class ListWorkerCertification(generic.ListView):
    template_name = 'cruds/docent/certifications.html'
    model = WorkerCertification

    def get_context_data(self, **kwargs):
        context = super(ListWorkerCertification, self).get_context_data(**kwargs)

        oponencys_paginator = Paginator(self.request.user.worker.certifications.all(), 15)
        certifications_page = self.request.GET.get('pag')
        if oponencys_paginator.count > 0:
            context['certifications'] = oponencys_paginator.get_page(certifications_page)

        return context


# DETAIL VIEWS
class DetailCourse(BSModalReadView):
    model = Course
    template_name = 'cruds/docent/detail_course.html'


class DetailCourseEdition(BSModalReadView):
    model = CourseEdition
    template_name = 'cruds/docent/detail_course_edition.html'
    
    
class DetailTribunal(BSModalReadView):
    model = Tribunal
    template_name = 'cruds/docent/detail_tribunal.html'


class DetailOponency(BSModalReadView):
    model = Oponency
    template_name = 'cruds/docent/detail_oponency.html'


class DetailWorkerCertification(BSModalReadView):
    model = WorkerCertification
    template_name = 'cruds/docent/detail_worker_certification.html'


# UPDATE VIEWS
class UpdateCourse(BSModalUpdateView):
    model = Course
    template_name = 'cruds/docent/update_course.html'
    form_class = forms.FormCourse
    success_message = 'El curso fue modificado satisfactoriamente.'


class UpdateCourseEdition(BSModalUpdateView):
    model = CourseEdition
    template_name = 'cruds/docent/update_course_edition.html'
    form_class = forms.FormCourseEdition
    success_message = 'El curso fue modificado satisfactoriamente.'


class UpdateTribunal(BSModalUpdateView):
    model = Tribunal
    template_name = 'cruds/docent/update_tribunal.html'
    form_class = forms.FormTribunal
    success_message = 'El tribunal fue modificado satisfactoriamente.'


class UpdateOponency(BSModalUpdateView):
    model = Oponency
    template_name = 'cruds/docent/update_oponency.html'
    form_class = forms.FormOponency
    success_message = 'El curso fue modificado satisfactoriamente.'


class UpdateWorkerCertification(BSModalUpdateView):
    model = WorkerCertification
    template_name = 'cruds/docent/update_worker_certification.html'
    form_class = forms.FormWorkerCertification
    success_message = 'El curso fue modificado satisfactoriamente.'


# DELETE VIEWS
class DeleteCourse(BSModalDeleteView):
    model = Course
    template_name = 'delete_element.html'
    success_url = reverse_lazy('piloto:courses')


class DeleteCourseEdition(BSModalDeleteView):
    model = CourseEdition
    template_name = 'delete_element.html'
    success_url = reverse_lazy('piloto:course_editions')


class DeleteTribunal(BSModalDeleteView):
    model = Tribunal
    template_name = 'delete_element.html'
    success_message = 'El tribunal fue eliminado de su CV satisfactoriamente.'
    success_url = reverse_lazy('piloto:tribunals')


class DeleteOponency(BSModalDeleteView):
    model = Oponency
    template_name = 'delete_element.html'
    success_message = 'La oponencia fue eliminada de su CV satisfactoriamente.'
    success_url = reverse_lazy('piloto:oponencys')


class DeleteWorkerCertification(BSModalDeleteView):
    model = WorkerCertification
    template_name = 'delete_element.html'
    success_message = 'La oponencia fue eliminada de su CV satisfactoriamente.'
    success_url = reverse_lazy('piloto:worker_certifications')


"""
class DeleteTutoria(BSModalDeleteView):
    model = Tutoria
    template_name = 'delete_element.html'
    success_message = 'La Tutoria fue eliminada de su CV satisfactoriamente.'
    success_url = reverse_lazy('piloto:perfil')
"""
