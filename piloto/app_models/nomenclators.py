from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    private_email = models.EmailField(null=True, blank=True)
    institutional_email = models.EmailField()
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    institutional_phone = models.CharField(max_length=20, null=True, blank=True)
    institutional_cellphone = models.CharField(max_length=20, null=True, blank=True)
    private_cellphone = models.CharField(max_length=20, null=True, blank=True)


class KnowledgeField(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CostCenter(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class StudyCenter(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Meteorologia, Informática, Cibernética, Física
class Field(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class WorkField(models.Model):
    CATEGORY = (
        ('Téc', 'Técnico'),
        ('Ing', 'Ingeniero'),
        ('Lic', 'Licenciado'),
    )

    category = models.CharField(max_length=50, choices=CATEGORY)
    field = models.ForeignKey(Field, on_delete=models.DO_NOTHING)
    study_center = models.ForeignKey(StudyCenter, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.category + ' ' + self.field.name


class Occupation(models.Model):
    GROUP = (
        ('V', 'V'),
        ('VI', 'VI'),
        ('VII', 'VII'),
        ('VIII', 'VIII'),
        ('IX', 'IX'),
        ('X', 'X'),
        ('XI', 'XI'),
        ('XII', 'XII'),
        ('XIII', 'XIII'),
        ('XIV', 'XIV'),
        ('XV', 'XV'),
        ('XVI', 'XVI'),
        ('XVII', 'XVII'),
        ('XVIII', 'XVIII'),
        ('XIX', 'XIX'),
        ('XX', 'XX'),
        ('XXI', 'XXI'),
        ('XXII', 'XXII'),
        ('XXIII', 'XXIII'),
        ('XXIV', 'XXIV'),
        ('XXV', 'XXV'),)

    name = models.CharField(max_length=100, unique=True)
    older_group = models.CharField(max_length=10, choices=GROUP, blank=True, null=True)
    current_group = models.CharField(max_length=10, choices=GROUP)
    older_salary = models.FloatField(blank=True, null=True)
    current_salary = models.FloatField()

    def __str__(self):
        return self.name


class Office(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PeopleOrganism(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class PoliticOrganism(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Prize(models.Model):
    LEVEL = (
        ('CITMA', 'Ministerio de Ciencia, Tecnología y Medio Ambiente'),
        ('ACC', 'Academia de Ciencias'),
        ('MES', 'Ministerio de Educación Superior'),
        ('O', 'Otro'),
    )

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=LEVEL, null=True, blank=True)

    def __str__(self):
        return self.name


class Entity(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default='Cuba')

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    start = models.DateField()
    end = models.DateField()
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    LEVEL = (
        ('N', 'Nacional'),
        ('I', 'Internacional'),
    )

    date = models.DateField()
    name = models.CharField(max_length=500)
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING)
    level = models.CharField(max_length=20, choices=LEVEL)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



