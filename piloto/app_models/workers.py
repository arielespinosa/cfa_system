# Python
import datetime

# Django
import django
from django.db import models
from django.contrib.auth.models import User
from .nomenclators import (
    Contact, WorkField, Occupation, Office, PeopleOrganism, PoliticOrganism, Municipality, KnowledgeField
)


class Person(models.Model):
    SEX = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),)

    SCIENTIFIC_GRADE = (
        ('MSc', 'Master'),
        ('Dr', 'Doctor(a)'),)

    name = models.CharField(max_length=50)
    lastname1 = models.CharField(max_length=50)
    lastname2 = models.CharField(max_length=50)
    sex = models.CharField(max_length=20, choices=SEX)
    scientific_grade = models.CharField(max_length=50, choices=SCIENTIFIC_GRADE, null=True, blank=True)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.lastname1 + ' ' + self.lastname2

    @property
    def fullname(self):
        return self.name + ' ' + self.lastname1 + ' ' + self.lastname2

    def short_coloquial_name(self):
        if self.scientific_grade:
            return self.scientific_grade + '. ' + self.name + ' ' + self.lastname1
        else:
            return self.name + ' ' + self.lastname1

    @property
    def coloquial_name(self):
        if self.scientific_grade:
            return self.scientific_grade + '. ' + self.name + ' ' + self.lastname1 + ' ' + self.lastname2
        else:
            return self.fullname


class ExternalPerson(Person):
    app_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)


class Worker(Person):
    WORK_CATEGORY = (
        ('T', 'Técnico'),
        ('E', 'Especialista'),
    )

    WORK_STATUS = (
        ('AP', 'A prueba'),
        ('F', 'Fijo'),)

    SKIN_COLOR = (
        ('B', 'Blanca'),
        ('M', 'Mestiza'),
        ('N', 'Negra'),)

    SCHOLAR_LVL = (
        ('M', 'Medio'),
        ('S', 'Superior'),)

    SCIENTIFIC_CATEGORY = (
        ('AI', 'Aspirante a Investigador'),
        ('IA', 'Investigador Agregado'),
        ('IT', 'Investigador Titular'),)

    DOCENT_CATEGORY = (
        ('PI', 'Profesor Instructor'),
        ('PS', 'Profesor Asistente'),
        ('PX', 'Profesor Auxiliar'),
        ('PA', 'Profesor Agregado'),
        ('PT', 'Profesor Titular'),
    )

    app_user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='fotos_de_perfiles/', default='avatar_default.jpg', null=True)
    ci = models.CharField(max_length=11)
    skin_color = models.CharField(max_length=20, choices=SKIN_COLOR)
    scholar_lvl = models.CharField(max_length=50, choices=SCHOLAR_LVL)
    work_field = models.ForeignKey(WorkField, on_delete=models.DO_NOTHING, blank=True, null=True)
    scientific_category = models.CharField(max_length=50, choices=SCIENTIFIC_CATEGORY, null=True, blank=True)
    docent_category = models.CharField(max_length=50, choices=DOCENT_CATEGORY, null=True, blank=True)
    card = models.IntegerField(unique=True)
    ocupation = models.ForeignKey(Occupation, on_delete=models.DO_NOTHING, blank=True, null=True)
    office = models.ForeignKey(Office, on_delete=models.DO_NOTHING, blank=True, null=True)
    work_category = models.CharField(max_length=20, choices=WORK_CATEGORY)
    in_insmet_date = models.DateField(default=django.utils.timezone.now)
    out_insmet_date = models.DateField(null=True, blank=True)
    out_motivations = models.TextField(max_length=1000, blank=True, null=True)
    res_34_19 = models.FloatField(blank=True, null=True)
    msc_dr = models.FloatField(blank=True, null=True)  # Lo que cobra por ser mst o phd
    other_old_payments = models.FloatField(blank=True, null=True)
    other_current_payments = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.DO_NOTHING, blank=True, null=True)
    politics_organisms = models.ManyToManyField(PoliticOrganism, null=True, blank=True)
    people_organisms = models.ManyToManyField(PeopleOrganism, null=True, blank=True)
    areas_of_interest = models.ManyToManyField(KnowledgeField, null=True, blank=True)

    def __str__(self):
        return self.coloquial_name

    @property
    def coloquial_name(self):
        if self.scientific_grade:
            return self.scientific_grade + '. ' + self.name + ' ' + self.lastname1 + ' ' + self.lastname2
        elif self.work_field:
            return self.work_field.category + '. ' + self.name + ' ' + self.lastname1 + ' ' + self.lastname2
        else:
            return self.name + ' ' + self.lastname1 + ' ' + self.lastname2

    def short_coloquial_name(self):
        if self.scientific_grade:
            return self.scientific_grade + '. ' + self.name + ' ' + self.lastname1
        elif self.work_field:
            return self.work_field.category + '. ' + self.name + ' ' + self.lastname1
        else:
            return self.name + ' ' + self.lastname1

    @property
    def born_date(self):
        return datetime.date(1991, 11, 28)

    @property
    def salario_total_antiguo(self):
        return 7

    @property
    def salario_total_actual(self):
        return 7

    @property
    def diferencia_salarial(self):
        return 7

    def display_ocupation(self):
        ocupation = self.ocupation.name
        pref = ocupation.split(' ')[0][:3] + '.'
        field = ocupation.split(' ')[-1]
        return pref + ' ' + field
    """
    def get_absolute_url(self):
        return reverse("recursos_humanos:perfil_trabajador", kwargs={"id":self.id})
    """
