from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse


class SingleCreateObjectMixin(object):

    def get_context_data(self, **kwargs):
        context = {}
        form = self.form_class(request=self.request)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():
            form.save()

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


class ListObjectPaginatorMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worker'] = self.request.user.worker

        paginator = Paginator(self.get_queryset(), 15)
        page = self.request.GET.get('pag')
        if paginator.count > 0:
            context['paginator'] = paginator.get_page(page)

        return context


class BSModalAjaxFormMixin(object):

    def get_data_as_json(self, form):
        return form.cleaned_data

    def form_invalid(self, form):
        response = super(BSModalAjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            datos = {
                'title': "Notificación",
                'message': self.error_message,
                # 'data': form.cleaned_data,
            }
            return JsonResponse(datos)
        else:
            # return JsonResponse(form.errors, status=400)
            print("no es Ajax")
            return response

    def form_valid(self, form):
        response = super(BSModalAjaxFormMixin, self).form_valid(form)

        if self.request.is_ajax():
            if form.is_valid():
                form.save(commit=False)
                form.author1 = self.request.user.appuser

                datos = {
                    'title': "Notificación",
                    'message': self.success_message,
                    # 'data': form.cleaned_data,
                }

            return JsonResponse(datos)
        else:
            return response

