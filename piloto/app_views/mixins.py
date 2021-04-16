from django import forms
from django.views import generic


class FormMixinPerson(forms.Form):

    class Meta:
        labels = {
            'ci': 'Carnet de Identidad',
            'lastname1': 'Primer apellido',
            'lastname2': 'Segundo apellido',
        }


class MixinListView(generic.ListView):

    def get_queryset(self, worker=None):
        if worker:
            return self.model.objects.filter(worker=worker)
        return self.model.objects.all()