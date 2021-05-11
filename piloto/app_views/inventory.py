from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.views import generic
from piloto.app_forms import inventory as frm_inventory


class CreateObject(BSModalCreateView):
    template_name = 'administrative/cruds/inventory/create_object.html'
    form_class = frm_inventory.FormObject
    success_message = 'El objeto se añadio satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

    def get_context_data(self, **kwargs):
        context = super(CreateObject, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    """
    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        form_crear_objeto = self.form_class(request.POST)
        form_crear_objeto.request = request

        if form_crear_objeto.is_valid():
            objeto = form_crear_objeto.save(commit=False)
            objeto.save()

            if request.is_ajax():
                return JsonResponse(data)
            else:
                return super(CrearObjeto, self).form_valid(form_crear_objeto)
        else:
            return super(CrearObjeto, self).post(request, *args, **kwargs)
    """


class CreateInventory(generic.CreateView):
    template_name = 'administrative/cruds/inventory/create_inventary.html'
    form_class = frm_inventory.FormInventory
    success_message = 'El inventario se añadio satisfactoriamente.'
    success_url = reverse_lazy('piloto:index')

    def get_context_data(self, **kwargs):
        context = super(CreateInventory, self).get_context_data(**kwargs)

        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    """
    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        form_crear_inventario = self.form_class(request.POST)
        form_crear_inventario.request = request

        if form_crear_inventario.is_valid():
            inventario = form_crear_inventario.save(commit=False)
            inventario.save()

            return JsonResponse(data)
        else:
            return super(CrearInventario, self).post(request, *args, **kwargs)
        """





