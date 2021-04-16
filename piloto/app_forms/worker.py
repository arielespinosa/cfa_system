from django import forms
from django.utils.translation import gettext_lazy as _
from piloto.app_models.workers import Worker, ExternalPerson
from piloto.app_models.nomenclators import Contact, KnowledgeField, Municipality
from bootstrap_modal_forms.forms import BSModalForm


class FormKnowledgeField(BSModalForm):
    class Meta:
        model = KnowledgeField
        fields = '__all__'


class FormMunicipality(BSModalForm):
    class Meta:
        model = Municipality
        fields = '__all__'


class FormContact(BSModalForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'private_email': _('Correo personal'),
            'institutional_email': _('Correo institucional'),
            'home_phone': _('Teléfono fijo personal'),
            'institutional_phone': _('Teléfono fijo institucional'),
            'institutional_cellphone': _('Teléfono celular institucional'),
            'private_cellphone': _('Teléfono celular personal'),
        }


class FormExternalPerson(BSModalForm):
    class Meta:
        model = ExternalPerson
        exclude = ['contact']
        labels = {
            'name': _('Nombre(s)'),
            'lastname1': _('Primer apellido'),
            'lastname2': _('Segundo apellido'),
            'sex': _('Sexo'),
            'scientific_grade': _('Grado científico'),
        }


class FormWorker(forms.ModelForm):
    class Meta:
        model = Worker
        exclude = ['user']


class FormEditWorker(BSModalForm):
    class Meta:
        model = Worker
        fields = '__all__'
        help_texts = {
            'name': 'El nombre es sensible a las mayúsculas',
        }

