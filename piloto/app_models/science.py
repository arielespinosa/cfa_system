import datetime
import django
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from gm2m import GM2MField
from .workers import Worker, ExternalPerson
from .nomenclators import (StudyCenter, Field, Prize, CostCenter, Program, Entity, Client, Task, Event)


class Ponency(models.Model):
    title = models.CharField(max_length=100)
    authors = GM2MField(Worker, ExternalPerson, related_name='ponencys')

    def __str__(self):
        return self.title

    @property
    def type(self):
        return 'Ponencia'


class PonencyRealized(models.Model):
    PARTICIPATION = (
        ('API_CO', 'Autor Principal Invitado por CO'),
        ('PAP', 'Ponente Autor Principal'),
        ('P', 'Ponente'),
    )
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    ponency = models.ForeignKey(Ponency, on_delete=models.DO_NOTHING, related_name='editions')
    participation = models.CharField(max_length=40, choices=PARTICIPATION)
    worker = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.ponency.title


class Comision(models.Model):
    creation_date = models.DateField()
    integrants = GM2MField(Worker, ExternalPerson, related_name='comisiones')

    @property
    def type(self):
        return 'Comision'

    def __str__(self):
        return 'Comision ' + str(self.pk)


class ScienceElement(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Thesis(ScienceElement):
    GRADE = (
        ('S', 'Superior'),
        ('MSc', 'Master'),
        ('Dr', 'Doctorado'),
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    grade = models.CharField(max_length=10, choices=GRADE)
    field = models.ForeignKey(Field, on_delete=models.DO_NOTHING)
    study_center = models.ForeignKey(StudyCenter, on_delete=models.DO_NOTHING)
    start_date = models.DateField(default=django.utils.timezone.now)
    end_date = models.DateField(null=True, blank=True)
    end_date_tutor = models.DateField(null=True, blank=True)
    student = GenericForeignKey('content_type', 'object_id')
    tutors = GM2MField(Worker, ExternalPerson, related_name='thesis_tutoradas')

    @property
    def type(self):
        return 'Tesis'

    @property
    def in_process(self):
        return True if not self.end_date_tutor else False

    @property
    def degree_title(self):
        return self.grade + ' en ' + self.field.name


class Article(ScienceElement):
    LEVEL = (
        ('I',  'Grupo I'),
        ('II', 'Grupo II'),
        ('III', 'Grupo III'),
        ('IV', 'Grupo IV'),
    )

    PARTICIPATION = (
        ('AP', 'Autor Principal'),
        ('OA', 'Otro Autor'),
    )

    STATUS = (
        ('1', 'Enviado'),
        ('2', 'En revision'),
        ('3', 'Aceptado'),
        ('4', 'Publicado'),
    )

    doi = models.CharField(max_length=50, unique=True)
    authors = GM2MField(Worker, ExternalPerson, related_name='articles')
    database = models.CharField(max_length=100, null=True, blank=True)
    pages = models.CharField(max_length=50)
    pub_date = models.DateField(default=django.utils.timezone.now, null=True)
    web_url = models.URLField(null=True, blank=True)
    magazine = models.CharField(max_length=200, null=True, blank=True)
    issn = models.CharField(max_length=50, unique=True, null=True, blank=True)
    volume = models.PositiveSmallIntegerField(null=True, blank=True)
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    impact_level = models.CharField(max_length=50, choices=LEVEL, null=True, blank=True)
    participation = models.CharField(max_length=50, choices=PARTICIPATION)
    indexed = models.BooleanField(default=False)
    refereed = models.BooleanField(default=False)
    gray_literature = models.BooleanField(default=False)

    @property
    def type(self):
        return 'Artículo'


class Result(ScienceElement):
    LEVEL = (
        ('1', 'Primer Nivel'),
        ('2', 'Segundo Nivel'),
        ('3', 'Tercer Nivel'),
    )
    date = models.DateField(default=django.utils.timezone.now)
    manager_by_cfa = models.BooleanField(default=True)
    approved_by_cc = models.BooleanField(default=False)
    prize = models.ManyToManyField(Prize, null=True, blank=True)
    level = models.CharField(max_length=40, choices=LEVEL)
    integrants = GM2MField(Worker, ExternalPerson, related_name='results')

    @property
    def type(self):
        return 'Resultado'


class Project(ScienceElement):
    LEVEL = (
        ('PP', 'Programa Priorizado'),
        ('PE', 'Proyecto Empresarial'),
        ('INF', 'Institucional ft'),
        ('IN', 'Institucional'),
    )

    TYPE = (
        ('N', 'Nacional'),
        ('I', 'Internacional'),
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    cost_center = models.ForeignKey(CostCenter, on_delete=models.DO_NOTHING)
    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING, null=True, blank=True)
    boss = GenericForeignKey('content_type', 'object_id')
    participants = GM2MField(Worker, ExternalPerson, related_name='projects')
    manager_by_cfa = models.BooleanField(default=False)
    type = models.CharField(max_length=40, choices=TYPE)
    level = models.CharField(max_length=40, choices=LEVEL, blank=True, null=True)
    aproved_date = models.DateField(default=datetime.datetime.now())
    start_date = models.DateField(default=datetime.datetime.now())
    end_plan_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    executor_entity = models.ForeignKey(Entity, on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    results = models.ManyToManyField(Result, null=True, blank=True)
    entity = models.ManyToManyField(Entity, related_name="entities", null=True, blank=True)
    #manager = ProyectoManager()

    @property
    def type(self):
        return 'Proyecto'

    @property
    def en_desarrollo(self):
        return True if not self.end_date else False

    @property
    def en_atraso(self):
        return True if not self.end_date and self.end_date > datetime.date.now() else False

    def for_next_year(self):
        return True if self.aproved_date.year > datetime.date.now().year else False


class Book(ScienceElement):
    isbn = models.CharField(max_length=50)
    authors = GM2MField(Worker, ExternalPerson, related_name='books')
    data_base = models.CharField(max_length=100, null=True, blank=True) # que es esto?
    pages = models.CharField(max_length=50) # cant de pages?
    pub_date = models.DateField(default=django.utils.timezone.now)
    web_url = models.URLField(null=True, blank=True)
    editorial = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    chapter = models.CharField(max_length=50) # cant de capitulos?
    total_pages = models.CharField(max_length=50) # no deberia ser entero?
    gray_literature = models.BooleanField(default=False)

    @property
    def type(self):
        return 'Libro'


class Service(models.Model):
    TIPO = (
        ('EST', 'Estatal'),
        ('COM', 'Comercial'),
        ('EXP', 'Exportación'),
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    start_date = models.DateField(default=django.utils.timezone.now())
    end_date = models.DateField()
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=20, choices=TIPO, blank=True, null=True)
    dim = models.CharField(max_length=50, blank=True, null=True)
    cost_center = models.ForeignKey(CostCenter, on_delete=models.DO_NOTHING)
    participants = GM2MField(Worker, ExternalPerson, related_name='services')
    responsible = GenericForeignKey('content_type', 'object_id')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    mont = models.FloatField(default=0.0)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    results = models.ManyToManyField(Result, null=True, blank=True)
    tasks = models.ManyToManyField(Task, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def type(self):
        return 'Service'


class SciencePrize(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    date = models.DateField()
    prize = models.ForeignKey(Prize, on_delete=models.DO_NOTHING)
    element = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.prize.name



