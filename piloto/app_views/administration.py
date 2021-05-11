from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.views import generic
from piloto.app_forms import inventory as frm_inventory


class AdministrativeWorkView(generic.TemplateView):
    template_name = 'administrative/administrative_work.html'

    def get_context_data(self, **kwargs):
        context = super(AdministrativeWorkView, self).get_context_data(**kwargs)
        return context



