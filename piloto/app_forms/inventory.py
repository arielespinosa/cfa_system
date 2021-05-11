from django import forms
from django.utils.translation import gettext_lazy as _
from piloto.app_models.inventory import Object, Inventory
from piloto.app_models.workers import Worker, ExternalPerson
from bootstrap_modal_forms.forms import BSModalForm
from cfa_system.mixins.forms import FlexibleCrispyForm


class FormObject(BSModalForm):
    class Meta:
        model = Object
        fields = '__all__'


class FormInventory(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
