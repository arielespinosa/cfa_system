from datetime import date
from django import forms
from django.utils.translation import gettext_lazy as _
from bootstrap_modal_forms.forms import BSModalForm
from cfa_system.mixins.forms import FlexibleCrispyForm
from piloto.app_models.workers import Worker
from piloto.app_models.science import (
    Ponency, PonencyRealized, Comision, Thesis, Project, Article, Service, Book, Result, SciencePrize
)
from piloto.app_models.nomenclators import Event

from .utils import all_persons_choices, work_field_choices, scientific_elements_choices


class FormProjects(BSModalForm):
    class Meta:
        model = Project
        fields = ['cost_center', 'title', 'program']


class FormArticles(BSModalForm):
    class Meta:
        model = Article
        fields = '__all__'


class FormBooks(BSModalForm):
    project = forms.IntegerField()

    class Meta:
        model = Book
        fields = '__all__'


class FormResults(BSModalForm):
    project = forms.IntegerField()

    class Meta:
        model = Result
        fields = '__all__'


# Forms  -----------------------------
class FormPonency(BSModalForm):
    authors = forms.MultipleChoiceField(choices=[], required=False, label='Autores')

    class Meta:
        model = Ponency
        fields = '__all__'
        labels = {
            'title': _('Título'),
            'authors': _('Autores'),
        }

    @property
    def is_empity(self):
        return False

    def __init__(self, *args, **kwargs):
        super(FormPonency, self).__init__(*args, **kwargs)
        #self.fields['authors'].choices = all_persons_choices(self.request.user.worker)
        self.fields['authors'].choices = all_persons_choices()


class FormPonencyRealized(forms.ModelForm):
    event = forms.ModelChoiceField(label='Evento', queryset=Event.objects.all(),widget=forms.Select(attrs={'class': 'chosen-select', 'placeholder': 'Eventos...'}))
    ponency = forms.ModelChoiceField(label='Ponencia', queryset=None, widget=forms.Select(attrs={'class': 'chosen-select', 'placeholder': 'Ponencias...'}), required=False)

    class Meta:
        model = PonencyRealized
        exclude = ['worker']
        labels = {
            'event': _('Evento'),
            'ponency': _('Ponencia'),
            'participation': _('Participación')
        }

    def __init__(self, request=None, *args, **kwargs):
        super(FormPonencyRealized, self).__init__(*args, **kwargs)
        if request:
            self.fields['ponency'].queryset = request.user.worker.ponencys.all()

        
      
 
    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False


class FormComision(FlexibleCrispyForm, forms.ModelForm):
    integrants = forms.MultipleChoiceField(choices=[], label='Integrantes')

    class Meta:
        model = Comision
        fields = '__all__'
        labels = {
            'creation_date': _('Fecha de creación'),
            'integrants': _('Integrantes')
        }

    def __init__(self, request=None, *args, **kwargs):
        super(FormComision, self).__init__(*args, **kwargs)
        self.fields['integrants'].choices = all_persons_choices(request.user.worker)


class FormThesis(FlexibleCrispyForm, forms.ModelForm):
    student = forms.ChoiceField(choices=[], required=False, label='Estudiante')
    tutors = forms.MultipleChoiceField(choices=[], label='Tutores')
    
    class Meta:
        model = Thesis
        exclude = ['content_type', 'object_id']
        labels = {
            'title': _('Título'),
            'grade': _('Grado'),
            'field': _('Campo'),
            'study_center': _('Centro de estudios'),
            'start_date': _('Fecha de inicio'),
            'end_date': _('Fecha de culminación'),
            'end_date_tutor': _('Fecha de culminación de tutoría'),
            'tutors': _('Tutores'),
        }
        widgets = {
            'student': forms.Select(attrs={'id': 'id_student'}),
        }

    def __init__(self, request=None, *args, **kwargs):
        super(FormThesis, self).__init__(*args, **kwargs)
        self.fields['student'].choices = all_persons_choices()
        self.fields['tutors'].choices = all_persons_choices()

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']
        if start_date > date.today():
            raise forms.ValidationError("No pude ser futuro.")
        return start_date

    def clean(self):
        cleaned_data = super().clean()
        
        student = cleaned_data.get('student')
        tutors = cleaned_data.get('tutors')
        
        if student in tutors:
            self.add_error('student', "El estudiante y el tutor no pueden ser la misma persona")
            self.add_error('tutors', "El estudiante y el tutor no pueden ser la misma persona")     
        return cleaned_data


class FormProject(FlexibleCrispyForm, forms.ModelForm):
    boss = forms.ChoiceField(choices=[], label='Jefe')
    participants = forms.MultipleChoiceField(choices=[], label='Participantes')
    
    class Meta:
        model = Project
        exclude = ['content_type', 'object_id']
        labels = {
            'title': _('Título'),
            'cost_center':_('Centro de costo'),
            'program': _('Programa'),
            'boss': _('Jefe'),
            'participants':_('Participantes'),
            'manager_by_cfa':_('Dirigido por el CFA'),
            'type':_('Tipo'),
            'level':_('Nivel'),
            'aproved_date':_('Fecha de aprovación'),
            'start_date':_('Fecha de inicio'),
            'end_plan_date':_('Fecha de culminación planificada'),
            'end_date':_('Fecha de culminación'),
            'executor_entity':_('Entidad ejecutora'),
            'description':_('Descripción'),
            'results':_('Resultados'),
            'entity':_('Entidades participantes'),
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

    def __init__(self, request, *args, **kwargs):
        super(FormProject, self).__init__(*args, **kwargs)
        self.fields['boss'].choices = all_persons_choices()
        self.fields['participants'].choices = all_persons_choices(request.user.worker)


class FormArticle(FlexibleCrispyForm, forms.ModelForm):
    authors = forms.MultipleChoiceField(choices=[], label='Autores')

    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'title':_('Título'),
            'doi':_('DOI'),
            'authors':_('Autores'),
            'database':_('Base de datos'),
            'pages':_('Páginas'),
            'pub_date':_('Fecha de publicación'),
            'web_url':_('URL'),
            'magazine':_('Revista'),
            'issn':_('ISSN'),
            'volume':_('Volumen'),
            'number':_('Número'),
            'impact_level':_('Impacto'),
            'participation':_('Participación'),
            'indexed':_('Indexado'),
            'refereed':_('Arbitrado'),
            'gray_literature':_('Literatura gris'),
        }
        widgets = {          

        }

    def __init__(self, request, *args, **kwargs):
        super(FormArticle, self).__init__(*args, **kwargs)
        self.fields['authors'].choices = all_persons_choices(request.user.worker)
    
    def clean_pub_date(self):
        fecha = self.cleaned_data['pub_date']
        if fecha > date.today():
            raise forms.ValidationError("No pude ser futuro.")
        return fecha


class FormBook(FlexibleCrispyForm, forms.ModelForm):
    authors = forms.MultipleChoiceField(choices=[], label='Autores')

    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': _('Título'),
            'isbn': _('ISBN'),
            'authors': _('Autores'),
            'database': _('Base de datos'),
            'pages': _('Páginas'),
            'pub_date': _('Fecha de publicación'),
            'web_url': _('URL'),
            'editorial': _('Editorial'),
            'country': _('País'),
            'chapter': _('Capítulo'),
            'total_pages': _('Cantidad de páginas'),
            'gray_literature': _('Literatura gris'),
        }
        widgets = {          

        }

    def __init__(self, request, *args, **kwargs):
        super(FormBook, self).__init__(*args, **kwargs)
        self.fields['authors'].choices = all_persons_choices(request.user.worker)

    def clean_pub_date(self):
        fecha = self.cleaned_data['pub_date']
        if fecha > date.today():
            raise forms.ValidationError("No pude ser futuro")
        return fecha


class FormResult(FlexibleCrispyForm, forms.ModelForm):
    integrants = forms.MultipleChoiceField(choices=[], label='Integrantes')

    class Meta:
        model = Result
        fields = '__all__'
        labels = {
            'title': _('Título'),
            'date': _('Fecha'),
            'manager_by_cfa': _('Dirigido por CFA'),
            'approved_by_cc': _('Aprobado por CC'),
            'prize': _('Premios'),
            'level': _('Nivel'),
        }

    def __init__(self, request=None, *args, **kwargs):
        super(FormResult, self).__init__(*args, **kwargs)
        self.fields['integrants'].choices = all_persons_choices(request.user.worker)


class FormService(FlexibleCrispyForm, BSModalForm):
    responsible = forms.ChoiceField(choices=[], label='Responsable')
    participants = forms.MultipleChoiceField(choices=[], required=False, label='Participantes')
    
    class Meta:
        model = Service
        exclude = ['content_type', 'object_id']
        labels = {
            'start_date': _('Fecha de inicio'),
            'end_date': _('Fecha de terminación'),
            'name': _('Nombre'),
            'type': _('Tipo'),
            'dim': _('DIM'),
            'cost_center': _('Centro de costo'),
            'participants': _('Participantes'),
            'responsible': _('Responsable'),
            'client': _('Cliente'),
            'mont': _('Monto'),
            'entity': _('Entidad'),
            'results': _('Resultados'),
            'tasks': _('Tareas'),
        }
        widgets = {            

        }

    def __init__(self, request=None, *args, **kwargs):
        super(FormService, self).__init__(*args, **kwargs)
        self.fields['responsible'].choices = all_persons_choices()
        self.fields['participants'].choices = all_persons_choices(request.user.worker)

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']

        if start_date > date.today():
            raise forms.ValidationError("No pude ser futuro.")
        return start_date

    def clean_end_date(self):
        end_date = self.cleaned_data['end_date']
     
        if end_date < date.today():
            raise forms.ValidationError("No pude ser pasado.")
        return end_date

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        """
        if start_date > end_date:
            raise forms.ValidationError("La fecha de iniicio no pude ser mayor a la fecha de terminación.")
        if end_date < start_date:
            raise forms.ValidationError("La fecha de terminación no pude ser menor a la fecha de inicio.")
        """


class FormSciencePrize(FlexibleCrispyForm, forms.ModelForm):
    element = forms.ChoiceField(choices=[], label='Elemento')

    class Meta:
        model = SciencePrize
        exclude = ['content_type', 'object_id']
        labels = {
            'date': _('Fecha'),
            'prize': _('Premio'),
            'element': _('Elemento'),
        }
        widgets = {

        }

    def __init__(self, *args, **kwargs):
        super(FormSciencePrize, self).__init__(*args, **kwargs)
        self.fields['element'].choices = scientific_elements_choices()
 

