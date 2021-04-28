from django.shortcuts import render, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import JsonResponse
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from cfa_system.mixins.mixins_views import SingleCreateObjectMixin, ListObjectPaginatorMixin
from piloto.app_models.nomenclators import Client, Field, StudyCenter
from piloto.app_models.workers import Worker, ExternalPerson
from piloto.app_models.science import *
from piloto.app_forms import science as forms
from piloto.app_views.mixins import MixinListView


class WorkerScienceWorkView(generic.TemplateView):
    template_name = 'cruds/science/worker_science_work.html'


# CREATE VIEWS
class CreatePonency(BSModalCreateView):
    template_name = 'cruds/science/create_ponency.html'
    form_class = forms.FormPonency
    success_message = 'La ponencia se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:create_ponency_realized')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():
            element = form.save(commit=False)
            element.save()

            authors = request.POST.getlist('authors', None)

            if authors:
                if not (request.user.worker.pk in authors):
                    element.authors.add(request.user.worker)

                for author_pk in authors:
                    try:
                        author = Worker.objects.get(pk=author_pk)
                    except ObjectDoesNotExist:
                        author = ExternalPerson.objects.get(pk=author_pk)
                    element.authors.add(author)
            else:
                element.authors.add(request.user.worker)

            if request.is_ajax():
                data = {
                    'title': "Notificación",
                    'message': self.success_message,
                }
                return JsonResponse(data)
            else:
                return HttpResponseRedirect(self.success_url)
        else:
            return super().post(request, *args, **kwargs)


class CreatePonencyRealized(generic.CreateView):
    template_name = 'cruds/science/create_ponency_realized.html'
    form_class = forms.FormPonencyRealized
    success_message = 'La ponencia se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:ponencys')

    def get_context_data(self, **kwargs):
        context = super(CreatePonencyRealized, self).get_context_data(**kwargs)
        context['form'] = self.form_class(request=self.request)
        return context
    
    def post(self, request, *args, **kwargs):

        PonencyRealized.objects.create(event=Event.objects.get(pk=8), ponency=Ponency.objects.get(pk=2), participation='PAP', worker=request.user.worker)
        #form = self.form_class(data=request.POST)
        #form.request = request

        #print(form.is_valid(), form.errors)
        #element = form.save(commit=False)
        #element.worker = request.user.worker
        #element.save()
        return HttpResponseRedirect(self.success_url)
 
        if form.is_valid():
            element = form.save(commit=False)
            element.worker = request.user.worker
            element.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return super().post(request, *args, **kwargs)


class CreateComision(SingleCreateObjectMixin, generic.CreateView):
    template_name = 'cruds/science/create_comision.html'
    form_class = forms.FormComision
    success_message = 'La Thesis se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:comisions')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            element = form.save(commit=False)
            element.save()
            element.integrants.add(request.user.worker)

            for integrant_pk in request.POST.getlist('id_integrants'):
                try:
                    integrant = Worker.objects.get(pk=integrant_pk)
                except ObjectDoesNotExist:
                    integrant = ExternalPerson.objects.get(pk=integrant_pk)
                element.integrants.add(integrant)

            return HttpResponseRedirect(self.success_url)
        else:
            return super().post(request, *args, **kwargs)


class CreateThesis(SingleCreateObjectMixin, generic.CreateView):
    template_name = 'cruds/science/create_thesis.html'
    form_class = forms.FormThesis
    success_message = 'La Thesis se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:thesis')

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        form_thesis = self.get_form(self.form_class)
        form_thesis.request = request

        if form_thesis.is_valid():
            student_pk = request.POST.get('student')
            try:
                student = Worker.objects.get(pk=student_pk)
            except ObjectDoesNotExist:
                student = ExternalPerson.objects.get(pk=student_pk)

            thesis = form_thesis.save(commit=False)
            thesis.student = student
            thesis.save()

            print(thesis.student)

            for tutor_pk in request.POST.getlist('tutors'):
                try:
                    tutor = Worker.objects.get(pk=tutor_pk)
                except:
                    tutor = ExternalPerson.objects.get(pk=tutor_pk)
                finally:
                    thesis.tutors.add(tutor)
            """
            for tutor in thesis.tutors.all():
                try:
                    if not tutor.tutorias.get(thesis__pk=thesis.pk):
                        tutor.tutoria_set.create(start_date=thesis.start_date, thesis=thesis)
                except:
                    pass
            """

            return HttpResponseRedirect(self.success_url)
        else:
            return super(CreateThesis, self).post(request, *args, **kwargs)


class CreateService(SingleCreateObjectMixin, generic.CreateView):
    template_name = 'cruds/science/create_service.html'
    form_class = forms.FormService
    success_message = 'El Service se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:services')

    def post(self, request, *args, **kwargs):
        form_service = self.form_class(request.POST)
        form_service.request = request

        if form_service.is_valid():
            responsible_pk = request.POST.get('responsible')
            try:
                responsible = Worker.objects.get(pk=responsible_pk)
            except:
                responsible = ExternalPerson.objects.get(pk=responsible_pk)

            service = form_service.save(commit=False)
            service.responsible = responsible
            service.save()

            participants = request.POST.getlist('participants')
            for participant_pk in participants:
                try:
                    participant = Worker.objects.get(pk=participant_pk)
                except ObjectDoesNotExist:
                    participant = ExternalPerson.objects.get(pk=participant_pk)
                service.participants.add(participant)
            service.participants.add(request.user.worker)

            data = {
                'title': "Notificación",
                'message': self.success_message,
            }
            return HttpResponseRedirect(self.success_url)
        else:
            return super(CreateService, self).post(request, *args, **kwargs)


class CreateProject(SingleCreateObjectMixin, generic.CreateView):
    template_name = 'cruds/science/create_project.html'
    form_class = forms.FormProject
    success_message = 'El Project se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:projects')

    def post(self, request, *args, **kwargs):
        form_project = self.form_class(request.POST)
        form_project.request = request

        if form_project.is_valid():
            boss_pk = request.POST.get('boss')
            try:
                boss = Worker.objects.get(pk=boss_pk)
            except ObjectDoesNotExist:
                boss = ExternalPerson.objects.get(pk=boss_pk)

            project = form_project.save(commit=False)
            project.boss = boss
            project.save()

            participants = request.POST.getlist('participants')
            for participant_pk in participants:
                try:
                    participant = Worker.objects.get(pk=participant_pk)
                except ObjectDoesNotExist:
                    participant = ExternalPerson.objects.get(pk=participant_pk)
                project.participants.add(participant)
            project.participants.add(request.user.worker)

            data = {
                'title': "Notificación",
                'message': self.success_message,
            }

            return HttpResponseRedirect(self.success_url)
        else:
            return super(CreateProject, self).post(request, *args, **kwargs)


class CreateArticle(SingleCreateObjectMixin, generic.CreateView):
    template_name = 'cruds/science/create_article.html'
    form_class = forms.FormArticle
    success_message = 'El artículo se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:articles')

    def post(self, request, *args, **kwargs):
        form_article = self.get_form(self.form_class)
        form_article.request = request

        if form_article.is_valid():
            article = form_article.save(commit=False)
            article.save()

            for autor_pk in request.POST.get('authors'):
                try:
                    author = Worker.objects.get(pk=autor_pk)
                except ObjectDoesNotExist:
                    author = ExternalPerson.objects.get(pk=autor_pk)
                article.authors.add(author)
            article.authors.add(request.user.worker)

            return HttpResponseRedirect(self.success_url)
        else:
            return super(CreateArticle, self).post(request, *args, **kwargs)


class CreateBook(SingleCreateObjectMixin, generic.CreateView):
    template_name = 'cruds/science/create_book.html'
    form_class = forms.FormBook
    success_message = 'El tribunal se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:books')

    def post(self, request, *args, **kwargs):
        form_book = self.get_form(self.form_class)
        form_book.request = request

        if form_book.is_valid():
            book = form_book.save(commit=False)
            book.save()

            for author_pk in request.POST.get('authors'):
                try:
                    author = Worker.objects.get(pk=author_pk)
                except ObjectDoesNotExist:
                    author = ExternalPerson.objects.get(pk=author_pk)
                book.authors.add(author)
            book.authors.add(request.user.worker)

            return HttpResponseRedirect(self.success_url)
        else:
            return super(CreateBook, self).post(request, *args, **kwargs)


class CreateResult(SingleCreateObjectMixin, generic.CreateView):
    template_name = 'cruds/science/create_result.html'
    form_class = forms.FormResult
    success_message = 'El Result se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:results')

    def post(self, request, *args, **kwargs):
        form_result = self.form_class(request.POST)
        form_result.request = request

        if form_result.is_valid():
            result = form_result.save(commit=False)
            result.save()

            for author_pk in request.POST.get('integrants'):
                try:
                    author = Worker.objects.get(pk=author_pk)
                except ObjectDoesNotExist:
                    author = ExternalPerson.objects.get(pk=author_pk)
                result.integrants.add(author)
            result.integrants.add(request.user.worker)

            return HttpResponseRedirect(self.success_url)
        else:
            return super(CreateResult, self).post(request, *args, **kwargs)


class CreateSciencePrize(SingleCreateObjectMixin, generic.CreateView):
    template_name = 'cruds/science/create_science_prize.html'
    form_class = forms.FormSciencePrize
    success_message = 'El premio asociado se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:science_prizes')

    def post(self, request, *args, **kwargs):
        form_prizes = self.get_form(self.form_class)
        form_prizes.request = request

        if form_prizes.is_valid():
            element_pk = request.POST.get('element')

            try:
                element = Thesis.objects.get(pk=element_pk)
            except ObjectDoesNotExist:
                pass

            try:
                element = Article.objects.get(pk=element_pk)
            except ObjectDoesNotExist:
                pass

            try:
                element = Result.objects.get(pk=element_pk)
            except ObjectDoesNotExist:
                pass

            try:
                element = Project.objects.get(pk=element_pk)
            except ObjectDoesNotExist:
                pass

            try:
                element = Book.objects.get(pk=element_pk)
            except ObjectDoesNotExist:
                pass

            prize = form_prizes.save(commit=False)
            prize.element = element
            prize.save()

            return HttpResponseRedirect(self.success_url)
        else:
            return super(CreateSciencePrize, self).post(request, *args, **kwargs)


# LIST VIEWS
class ListPonency(ListObjectPaginatorMixin, generic.ListView):
    template_name = 'cruds/science/ponencys.html'
    model = Ponency


class ListPonencyRealized(ListObjectPaginatorMixin, generic.ListView):
    template_name = 'cruds/science/ponency_realized.html'
    model = PonencyRealized

    def get_queryset(self, worker=None):
        if worker:
            return PonencyRealized.objects.filter(worker=worker)
        return PonencyRealized.objects.all()

    def tbl_ajax_content(self, worker=None):
        data = []

        for ponency in self.get_queryset(worker=worker):
            checkbox = """
                   <td>
                     <label class='mt-checkbox mt-checkbox-single mt-checkbox-outline'>
                         <input type='checkbox' class='checkboxes' value='{}' />
                         <span></span>
                     </label>
                   </td>
               """.format(ponency.pk)

            authors = [author.coloquial_name for author in ponency.ponency.authors.all()]

            data.append(
                [checkbox, ponency.event.name, ponency.ponency.title, authors, ponency.participation, ''])
        return data

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse({
                "data": self.tbl_ajax_content(worker=request.user.worker)
            })
        else:
            return super(ListPonencyRealized, self).get(request, *args, **kwargs)


class ListComision(ListObjectPaginatorMixin, MixinListView):
    template_name = 'cruds/science/comisions.html'
    model = Comision

    def tbl_ajax_content(self, worker=None):
        data = []
        return data

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse({
                "data": self.tbl_ajax_content(worker=request.user.worker)
            })
        else:
            return super(ListComision, self).get(request, *args, **kwargs)


class ListThesis(ListObjectPaginatorMixin, MixinListView):
    template_name = 'cruds/science/thesis.html'
    model = Thesis

    def get_queryset(self, worker=None):
        if worker:
            return self.model.objects.filter(object_id=worker.pk)
        return self.model.objects.all()

    def tbl_ajax_content(self, worker=None):
        data = []

        for thesis in self.get_queryset(worker=worker):
            checkbox = """
                   <td>
                     <label class='mt-checkbox mt-checkbox-single mt-checkbox-outline'>
                         <input type='checkbox' class='checkboxes' value='{}' />
                         <span></span>
                     </label>
                   </td>
               """.format(thesis.pk)

            tutors = [tutor.coloquial_name for tutor in thesis.tutors.all()]

            data.append([checkbox, thesis.title, thesis.grade, thesis.field, thesis.study_center.name,
                         thesis.start_date, thesis.end_date, tutors, ''])
        return data

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse({
                "data": self.tbl_ajax_content(worker=request.user.worker)
            })
        else:
            return super(ListThesis, self).get(request, *args, **kwargs)


class ListService(ListObjectPaginatorMixin, MixinListView):
    template_name = 'cruds/science/services.html'
    model = Service

    def tbl_ajax_content(self, worker=None):
        data = []

        for service in worker.services.all():
            checkbox = """
                      <td>
                        <label class='mt-checkbox mt-checkbox-single mt-checkbox-outline'>
                            <input type='checkbox' class='checkboxes' value='{}' />
                            <span></span>
                        </label>
                      </td>
                  """.format(service.pk)

            participants = [participant.coloquial_name for participant in service.participants.all()]

            data.append([checkbox, service.name, service.start_date, service.end_date, service.responsible.coloquial_name,
                         participants, service.client.name, ''])
        return data

    def get(self, request, *args, **kwargs):
        #print("Aki estoy 0")
        if request.is_ajax():
            return JsonResponse({
                "data": self.tbl_ajax_content(worker=request.user.worker)
            })
        else:
            return super(ListService, self).get(request, *args, **kwargs)


class ListProject(ListObjectPaginatorMixin, MixinListView):
    template_name = 'cruds/science/projects.html'
    model = Project

    def get_queryset(self, worker=None):
        if worker:
            return worker.projects.all()
        return super(ListProject, self).get_queryset()

    def tbl_ajax_content(self, worker=None):
        data = []

        for project in self.get_queryset(worker=worker):
            checkbox = """
                      <td>
                        <label class='mt-checkbox mt-checkbox-single mt-checkbox-outline'>
                            <input type='checkbox' class='checkboxes' value='{}' />
                            <span></span>
                        </label>
                      </td>
                  """.format(project.pk)

            participants = [participant.coloquial_name for participant in project.participants.all()]

            data.append(
                [checkbox, project.title, project.start_date, project.end_date, project.boss.coloquial_name,
                 project.manager_by_cfa, participants, ''])
        return data

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse({
                "data": self.tbl_ajax_content(worker=request.user.worker)
            })
        else:
            return super(ListProject, self).get(request, *args, **kwargs)


class ListArticles(ListObjectPaginatorMixin, MixinListView):
    template_name = 'cruds/science/articles.html'
    model = Article

    def tbl_ajax_content(self, worker=None):
        data = []

        for article in worker.articles.all():
            checkbox = """
                        <td>
                          <label class='mt-checkbox mt-checkbox-single mt-checkbox-outline'>
                              <input type='checkbox' class='checkboxes' value='{}' />
                              <span></span>
                          </label>
                        </td>
                    """.format(article.pk)

            authors = [author.coloquial_name for author in article.authors.all()]

            data.append(
                [checkbox, article.title, article.pub_date, article.doi, article.impact_level,
                 article.participation, authors, ''])
        return data

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse({
                "data": self.tbl_ajax_content(worker=request.user.worker)
            })
        else:
            return super(ListArticles, self).get(request, *args, **kwargs)


class ListBooks(ListObjectPaginatorMixin, MixinListView):
    template_name = 'cruds/science/books.html'
    model = Book

    def tbl_ajax_content(self, worker=None):
        data = []

        for book in worker.books.all():
            checkbox = """
                        <td>
                          <label class='mt-checkbox mt-checkbox-single mt-checkbox-outline'>
                              <input type='checkbox' class='checkboxes' value='{}' />
                              <span></span>
                          </label>
                        </td>
                    """.format(book.pk)

            authors = [author.coloquial_name for author in book.authors.all()]

            data.append(
                [checkbox, book.title, book.pub_date, book.isbn, book.editorial, authors, ''])
        return data

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse({
                "data": self.tbl_ajax_content(worker=request.user.worker)
            })
        else:
            return super(ListBooks, self).get(request, *args, **kwargs)


class ListResults(ListObjectPaginatorMixin, MixinListView):
    template_name = 'cruds/science/results.html'
    model = Result

    def tbl_ajax_content(self, worker=None):
        data = []

        for result in self.get_queryset(worker=worker):
            checkbox = """
                           <td>
                             <label class='mt-checkbox mt-checkbox-single mt-checkbox-outline'>
                                 <input type='checkbox' class='checkboxes' value='{}' />
                                 <span></span>
                             </label>
                           </td>
                       """.format(result.pk)

            integrants = [integrant.coloquial_name for integrant in result.integrants.all()]

            data.append(
                [checkbox, result.title, result.date, result.manager_by_cfa, result.approved_by_cc, result.level,
                integrants, ''])
        return data

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse({
                "data": self.tbl_ajax_content(worker=request.user.worker)
            })
        else:
            return super(ListResults, self).get(request, *args, **kwargs)


class ListSciencePrize(ListObjectPaginatorMixin, generic.ListView):
    template_name = 'cruds/science/science_prize.html'
    model = SciencePrize

    def get_queryset(self):
        return SciencePrize.objects.filter(object_id=self.request.user.worker.pk)


# DELETES
class DeletePonency(BSModalDeleteView):
    model = Ponency
    template_name = 'delete_element.html'
    success_message = 'El elemento fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('piloto:ponencys')


class DeletePonencyRealized(BSModalDeleteView):
    model = PonencyRealized
    template_name = 'delete_element.html'
    success_message = 'El elemento fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('piloto:ponencys')


class DeleteComision(BSModalDeleteView):
    model = Comision
    template_name = 'delete_element.html'
    success_message = 'El elemento fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('piloto:comisions')


class DeleteThesis(BSModalDeleteView):
    model = Thesis
    template_name = 'delete_element.html'
    success_message = 'El elemento fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('piloto:thesis')


class DeleteService(BSModalDeleteView):
    model = Service
    template_name = 'delete_element.html'
    success_message = 'El elemento fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('piloto:services')


class DeleteProject(BSModalDeleteView):
    model = Project
    template_name = 'delete_element.html'
    success_message = 'El elemento fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('piloto:projects')


class DeleteArticle(BSModalDeleteView):
    model = Article
    template_name = 'delete_element.html'
    success_message = 'El elemento fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('piloto:articles')


class DeleteBook(BSModalDeleteView):
    model = Book
    template_name = 'delete_element.html'
    success_message = 'El elemento fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('piloto:services')


class DeleteResult(BSModalDeleteView):
    model = Result
    template_name = 'delete_element.html'
    success_message = 'El elemento fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('piloto:projects')


class DeleteSciencePrize(BSModalDeleteView):
    model = SciencePrize
    template_name = 'delete_element.html'
    success_message = 'El elemento fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('piloto:articles')


# DETAILS
class DetailPonency(BSModalReadView):
    model = Ponency
    template_name = 'cruds/science/detail_ponency.html'


class DetailPonencyRealized(BSModalReadView):
    model = PonencyRealized
    template_name = 'cruds/science/detail_ponency_realized.html'


class DetailComision(BSModalReadView):
    model = Comision
    template_name = 'cruds/science/detail_comision.html'


class DetailThesis(BSModalReadView):
    model = Thesis
    template_name = 'cruds/science/detail_thesis.html'


class DetailService(BSModalReadView):
    model = Service
    template_name = 'cruds/science/detail_service.html'


class DetailProject(BSModalReadView):
    model = Project
    template_name = 'cruds/science/detail_project.html'


class DetailArticle(BSModalReadView):
    model = Article
    template_name = 'cruds/science/detail_article.html'


class DetailBook(BSModalReadView):
    model = Book
    template_name = 'cruds/science/detail_book.html'


class DetailResult(BSModalReadView):
    model = Result
    template_name = 'cruds/science/detail_result.html'


class DetailSciencePrizet(BSModalReadView):
    model = SciencePrize
    template_name = 'cruds/science/detail_science_prize.html'


# UPDATES
class UpdatePonency(BSModalUpdateView):
    model = Ponency
    template_name = 'cruds/science/update_ponency.html'
    form_class = forms.FormPonency
    success_message = 'El aviso especial fue modificado satisfactoriamente.'
    success_url = reverse_lazy('piloto:ponencys')


class UpdatePonencyRealized(BSModalUpdateView):
    model = PonencyRealized
    template_name = 'cruds/science/update_ponency_realized.html'
    form_class = forms.FormPonencyRealized
    success_message = 'El aviso especial fue modificado satisfactoriamente.'
    success_url = reverse_lazy('piloto:ponencys')


class UpdateComision(BSModalUpdateView):
    model = Comision
    template_name = 'cruds/science/update_comision.html'
    form_class = forms.FormComision
    success_message = 'El aviso especial fue modificado satisfactoriamente.'
    success_url = reverse_lazy('piloto:comision')


class UpdateThesis(BSModalUpdateView):
    model = Thesis
    template_name = 'cruds/science/update_thesis.html'
    form_class = forms.FormThesis
    success_message = 'El aviso especial fue modificado satisfactoriamente.'
    success_url = reverse_lazy('piloto:thesis')


class UpdateService(BSModalUpdateView):
    model = Service
    template_name = 'cruds/science/update_service.html'
    form_class = forms.FormService
    success_message = 'El aviso especial fue modificado satisfactoriamente.'
    success_url = reverse_lazy('piloto:services')


class UpdateProject(BSModalUpdateView):
    model = Project
    template_name = 'cruds/science/update_project.html'
    form_class = forms.FormProject
    success_message = 'El aviso especial fue modificado satisfactoriamente.'
    success_url = reverse_lazy('piloto:projects')


class UpdateArticle(BSModalUpdateView):
    model = Article
    template_name = 'cruds/science/update_article.html'
    form_class = forms.FormArticle
    success_message = 'El aviso especial fue modificado satisfactoriamente.'
    success_url = reverse_lazy('piloto:articles')


class UpdateBook(BSModalUpdateView):
    model = Book
    template_name = 'cruds/science/update_book.html'
    form_class = forms.FormBook
    success_message = 'El aviso especial fue modificado satisfactoriamente.'
    success_url = reverse_lazy('piloto:books')


class UpdateResult(BSModalUpdateView):
    model = Result
    template_name = 'cruds/science/update_result.html'
    form_class = forms.FormResult
    success_message = 'El aviso especial fue modificado satisfactoriamente.'
    success_url = reverse_lazy('piloto:results')


class UpdateSciencePrize(BSModalUpdateView):
    model = SciencePrize
    template_name = 'cruds/science/update_ponency.html'
    form_class = forms.FormSciencePrize
    success_message = 'El aviso especial fue modificado satisfactoriamente.'
    success_url = reverse_lazy('piloto:science_prizes')

