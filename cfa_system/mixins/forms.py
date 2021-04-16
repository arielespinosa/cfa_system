from django.forms import ModelForm, TextInput, DateInput, EmailInput
from crispy_forms.helper import FormHelper
from cfa_system.utils.forms import OnlyAlphaNumCharField, OnlyNumbCharField, OnlyTextCharField


class FlexibleCrispyForm(ModelForm):

    def __init__(self, *args, **kwargs):
        try:
            self.request = kwargs.pop('request')
        except:
            pass

        super(FlexibleCrispyForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)

            if field:
                if type(field.widget) in (TextInput, DateInput, EmailInput, OnlyAlphaNumCharField , OnlyNumbCharField, OnlyTextCharField):
                    field.widget.attrs['placeholder'] = field.label

                    if type(field.widget) is DateInput:
                        field.widget.input_type = 'date'

        self.helper = FormHelper()
        #self.helper.form_show_labels = False
        self.helper.form_tag = False
        self.helper.disable_csrf = True



"""  
def thumbnail(image_path, width, height):
    absolute_url = posixpath.join(settings.MEDIA_URL, image_path)
    return '<img src="%s" alt="%s" class="widget-img" />' % (absolute_url, image_path)
"""

"""
class ImageWidget(forms.ClearableFileInput):
    template = '<div>%(image)s</div>' \
               '<div>%(clear_template)s</div>' \
               '<div>%(input)s</div>'

    def __init__(self, attrs=None, template=None, width=200, height=200):
        if template is not None:
            self.template = template
        self.width = width
        self.height = height
        super(ImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
        }
        if not self.is_required:
            checkbox_name = self.clear_checkbox_name(name)
            checkbox_id = self.clear_checkbox_id(checkbox_name)
            substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
            substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
            substitutions['clear'] = forms.CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})

        input_html = super(forms.ClearableFileInput, self).render(name, value, attrs)
        if value and hasattr(value, 'width') and hasattr(value, 'height'):
            image_html = thumbnail(value.name, self.width, self.height)
            output = self.template % {'input': input_html,
                                      'image': image_html,
                                      'clear_template': self.template_with_clear % substitutions}
        else:
            output = input_html
        return mark_safe(output)
"""



