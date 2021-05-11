from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from piloto.app_models.workers import Worker, ExternalPerson
from piloto.app_forms.utils import work_field_choices, courses_choices
from piloto.app_models.workers import SEX, SCIENTIFIC_GRADE

class DateInput(forms.DateInput):
    input_type = 'date'


class FormAuthentication(AuthenticationForm):
    username  = forms.CharField(min_length=1, label='Usuario', widget=forms.TextInput())
    password  = forms.CharField(min_length=1, label='Contraseña', widget=forms.PasswordInput(render_value=True))
    error_messages = {
        'invalid_login': "No se reconoce la combinación de nombre de usuario y contraseña."
                           "Note que ambos campos pueden ser sensibles a las mayúsculas.", 
        'inactive': "Su cuenta está inactiva. Póngase en contacto con el administrador para activarla.",        
    }
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    user_temp = None

                if user_temp is not None:
                    if user_temp.is_active:
                        raise forms.ValidationError(
                            self.error_messages['invalid_login'],
                            code='invalid_login',
                            params={'username': self.username_field.verbose_name},
                        )
                    else:
                        try:
                            #print(self.user_cache)
                            self.confirm_login_allowed(user_temp)
                        except:
                            raise forms.ValidationError(
                                self.error_messages['inactive'],
                                code='inactive',
                                params={'username': self.username_field.verbose_name},
                            )
                else:
                    try:
                        self.confirm_login_allowed(user_temp)
                    except:
                        raise forms.ValidationError(
                            self.error_messages['invalid_login'],
                            code='invalid_login',
                            params={'username': self.username_field.verbose_name},
                        )

        return self.cleaned_data


class FormUser(UserCreationForm):
    username = forms.CharField(min_length=1, label='Usuario', widget=forms.TextInput(attrs={'placeholder':'Nombre de suario'}))
    password1 = forms.CharField(min_length=1, label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}, render_value=True))
    password2 = forms.CharField(min_length=1, label='Repetir contraseña', widget=forms.PasswordInput(attrs={'placeholder':'Repetir contraseña'}, render_value=True))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': _('Nombre de usuario'),
            'password1': _('Contraseña'),
            'password2': _('Repetir contraseña')
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2


class FormExternalPerson(forms.ModelForm):

    class Meta:
        model = ExternalPerson
        exclude = ['app_user', 'contact']
        labels = {
            'lastname1': 'Primer apellido',
            'lastname2': 'Segundo apellido',
            'sex': 'Sexo',
            'scientific_grade': 'Grado Científico'
        }


class FormAccount(forms.Form):
    ci = forms.CharField(max_length=11, label='CI')
    name = forms.CharField(max_length=50, label='Nombre')
    lastname1 = forms.CharField(max_length=50, label='Primer apellido')
    lastname2 = forms.CharField(max_length=50, label='Segundo apellido')
    sex = forms.CharField(label='Sexo', widget=forms.Select(choices=SEX))
    scientific_grade = forms.CharField(label='Grado científico', widget=forms.Select(choices=SCIENTIFIC_GRADE))


class FormWorker(forms.ModelForm):
    #work_field = forms.ChoiceField(choices=[], required=False)

    class Meta:
        model = Worker
        exclude = ['app_user', 'contact']
        labels = {
            'ci': _('CI'),
            'name': _('Nombre(s)'),
            'lastname1': _('Primer apellido'),
            'lastname2': _('Segundo apellido'),
            'sex': _('Sexo'),
            'scientific_grade': _('Grado científico'),
            'skin_color': _('Color de piel'),
            'scholar_lvl': _('Nivel escolar'),
            'work_field': _('Campo'),
            'scientific_category': _('Categoría científica'),
            'docent_category': _('Categoría docente'),
            'card': _('Tarjeta'),
            'ocupation': _('Ocupación'),
            'office': _('Oficina'),
            'work_category': _('Categoría'),
            'in_insmet_date': _('Fecha de entrada'),
            'address': _('Dirección'),
            'municipality': _('Municipio'),
            'areas_of_interest': _('Áreas de interes'),

        }
        widgets = {
            'card': forms.TextInput,
            'res_34_19': forms.TextInput,
            'in_insmet_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(FormWorker, self).__init__(*args, **kwargs)
        #self.fields['work_field'].choices = work_field_choices()

