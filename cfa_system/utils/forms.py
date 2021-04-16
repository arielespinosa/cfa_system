from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def only_numbers(value):
    if value.isdigit() is False:
        raise ValidationError('Solo dígitos.')


class OnlyTextCharField(forms.CharField):
    default_validators = [RegexValidator(r'^[a-zA-Zñ ]*$', 'Solo texto.')]


class OnlyNumbCharField(forms.CharField):
    default_validators = [RegexValidator(r'^[0-9]*$', 'Solo numeros.')]


class OnlyAlphaNumCharField(forms.CharField):
    default_validators = [RegexValidator(r'^[0-9a-zA-Zñ ]*$', 'Solo caracteres alfanuméricos.')]