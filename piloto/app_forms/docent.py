from django import forms
from django.utils.translation import gettext_lazy as _
from bootstrap_modal_forms.forms import BSModalForm
from cfa_system.mixins.forms import FlexibleCrispyForm
from piloto.app_models.science import (Comision, Thesis, Article, Result, Project)
from piloto.app_models.docent import *
from .utils import all_persons_choices, courses_choices, scientific_elements_choices


class DateInput(forms.DateInput):
    input_type = 'date'


class FormCourses(FlexibleCrispyForm, forms.Form):
    courses = forms.MultipleChoiceField(label='Cursos en los que no ha participado', choices=[], required=False) 
    
    class Meta:
        fields = ['courses']

    def __init__(self, pworker=None, *args, **kwargs):
        super(FormCourses, self).__init__(*args, **kwargs)
        self.fields['courses'].choices = courses_choices(pworker)


class FormCourse(FlexibleCrispyForm, forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'title': _('Título'),
            'hours': _('Cantidad de horas'),
            'study_center': _('Centro de estudios'),
            'credits': _('Créditos'),
            'description': _('Descripción'),
            'certification': _('Certificación'),
        }

        widgets = {
            'study_center': forms.Select(attrs={'id': 'id_centro_estudios'}),
        }


class FormCourseEdition(FlexibleCrispyForm, forms.ModelForm):
    edition = forms.IntegerField(required=False)
    teacher = forms.ChoiceField(choices=[], label='Profesor')
    students = forms.MultipleChoiceField(choices=[], label='Estudiantes')

    class Meta:
        model = CourseEdition
        exclude = ['content_type', 'object_id', 'edition']
        labels = {
            'edition': _('Edición'),
            'teacher': _('Profesor'),
            'start_date': _('Fecha de inicio'),
            'end_date': _('Fecha de culminación'),
            'course': _('Curso'),
            'students': _('Estudiantes'),
        }
 
    @property
    def is_empity(self):
        self.is_valid()
        # print(self.clean())
        # print(self.fields.keys())
        return False

    def __init__(self, *args, **kwargs):
        super(FormCourseEdition, self).__init__(*args, **kwargs)
        self.fields['teacher'].choices = all_persons_choices()
        self.fields['students'].choices = all_persons_choices()

    def clean(self):
        cleaned_data = super().clean()
        teacher = cleaned_data.get('teacher')
        students = cleaned_data.get('students')

        if teacher in students:
            self.add_error('students', "El profesor no puede ser estudiante del curso.")
        return cleaned_data


class FormOponencys(forms.Form):
    oponencies = forms.ModelMultipleChoiceField(label='Oponencias en las que no ha participado', queryset=None, required=False)
    
    class Meta:
        fields = ['oponencies']


class FormOponency(FlexibleCrispyForm, forms.ModelForm):
    opponents = forms.MultipleChoiceField(choices=[], label='Oponentes', required=False)
    element = forms.ChoiceField(choices=[], label='Elemento')

    class Meta:
        model = Oponency
        fields = ['opponents', 'date', 'element']
        labels = {
            'date': _('Fecha'),
            'element': _('Elemento'),
            'opponents': _('Oponentes'),
        }

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False

    def __init__(self, request=None,*args, **kwargs):
        super(FormOponency, self).__init__(*args, **kwargs)
        self.fields['opponents'].choices = all_persons_choices(request.user.worker)
        self.fields['element'].choices = scientific_elements_choices()


class FormTribunals(forms.Form):
    tribunals = forms.ModelMultipleChoiceField(label='Tribunales en los que no ha participado', queryset=None, required=False)

    class Meta:
        fields = ['tribunals']


class FormTribunal(FlexibleCrispyForm, forms.ModelForm):
    members = forms.MultipleChoiceField(choices=[], label='Miembros', required=False , help_text='Los miembros seleccionados no tendrán la necesidad de añadirlo en sus curriculums.')

    class Meta:
        model = Tribunal
        fields = '__all__'
        labels = {
            'date': _('Fecha'),
            'thesis': _('Tesis'),
            'members': _('Miembros'),
        }

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False

    def __init__(self, request=None, *args, **kwargs):
        super(FormTribunal, self).__init__(*args, **kwargs)
        self.fields['members'].choices = all_persons_choices(request.user.worker)


class FormWorkerCertification(FlexibleCrispyForm, forms.ModelForm):
    
    class Meta:
        model = WorkerCertification
        exclude = ['worker']
        labels = {
            'date': _('Fecha'),
            'certification': _('Certificación'),
            'worker': _('Trabajador'),
        }

    def __init__(self, request=None, *args, **kwargs):
        super(FormWorkerCertification, self).__init__(*args, **kwargs)


class FormComision(FlexibleCrispyForm, forms.ModelForm):
    integrants = forms.MultipleChoiceField(choices=[], label='Integrantes')

    class Meta:
        model = Comision
        fields = '__all__'

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False
    
    def __init__(self, request=None, *args, **kwargs):
        super(FormComision, self).__init__(*args, **kwargs)
        self.fields['integrants'].choices = all_persons_choices(request.user.worker)


