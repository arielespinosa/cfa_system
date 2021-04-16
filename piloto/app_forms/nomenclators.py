from django import forms
from django.utils.translation import gettext_lazy as _
from piloto.app_models.nomenclators import *
from piloto.app_models.workers import Worker, ExternalPerson
from bootstrap_modal_forms.forms import BSModalForm
from cfa_system.mixins.forms import FlexibleCrispyForm


class FormCertifications(forms.Form):
    certifications = forms.ModelMultipleChoiceField(label='Certificaciones que no posee', queryset=None, required=False)
    
    class Meta:
        fields = ['certifications']


class FormEvent(FlexibleCrispyForm, BSModalForm):
    class Meta:
        model = Event
        fields = '__all__'
        labels = {
            'date': _('Fecha'),
            'name': _('Nombre'),
            'place': _('Lugar'),
            'level': _('Nivel'),
            'description': _('Descripción'),
        }

        
class FormCertification(BSModalForm):
    class Meta:
        model = Certification
        fields = '__all__'
        labels = {
            'name': _('Título'),
            'description': _('Descripción'),
        }


class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'private_email': _('Personal'),
            'institutional_email': _('Institucional'),
            'institutional_phone': _('Fijo institucional'),
            'institutional_cellphone': _('Celular institucional'),
            'private_cellphone': _('Celular personal'),
            'home_phone': _('Fijo personal'),
        }


class FormPrize(BSModalForm):
    class Meta:
        model = Prize
        fields = '__all__'


class FormEntity(BSModalForm):
    class Meta:
        model = Entity
        fields = '__all__'


class FormProgram(BSModalForm):
    class Meta:
        model = Program
        fields = '__all__'


class FormClient(BSModalForm):
    class Meta:
        model = Client
        fields = '__all__'


class FormCostCenter(BSModalForm):
    class Meta:
        model = CostCenter
        fields = '__all__'


class FormStudyCenter(BSModalForm):
    class Meta:
        model = StudyCenter
        fields = '__all__'


class FormKnowledgeField(BSModalForm):
    class Meta:
        model = KnowledgeField
        fields = '__all__'


class FormField(BSModalForm):
    class Meta:
        model = Field
        fields = '__all__'


class FormWorkField(BSModalForm):
    class Meta:
        model = WorkField
        fields = '__all__'


class FormOccupation(BSModalForm):
    class Meta:
        model = Occupation
        fields = '__all__'


class FormOffice(BSModalForm):
    class Meta:
        model = Office
        fields = '__all__'


class FormPeopleOrganism(BSModalForm):
    class Meta:
        model = PeopleOrganism
        fields = '__all__'


class FormPoliticOrganism(BSModalForm):
    class Meta:
        model = PoliticOrganism
        fields = '__all__'


class FormTask(BSModalForm):
    class Meta:
        model = Task
        fields = '__all__'


