from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from gm2m import GM2MField
from .workers import Worker, ExternalPerson
from .nomenclators import StudyCenter, Certification
from .science import Thesis


class Course(models.Model):
    title = models.CharField(max_length=100)
    hours = models.FloatField()
    study_center = models.ForeignKey(StudyCenter, on_delete=models.DO_NOTHING)
    credits = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    certification = models.ForeignKey(Certification, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class CourseEdition(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    edition = models.PositiveSmallIntegerField()
    teacher = GenericForeignKey('content_type', 'object_id')
    start_date = models.DateField()
    end_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(Worker, related_name='courses')

    def __str__(self):
        return self.course.title

    @property
    def name(self):
        return self.course.title

    def display_edition(self):
        return 'Edición #{}'.format(self.edition)


class WorkerCertification(models.Model):
    date = models.DateField()
    certification = models.ForeignKey(Certification, on_delete=models.DO_NOTHING)
    worker = models.ForeignKey(Worker, on_delete=models.DO_NOTHING, related_name='certifications')

    def __str__(self):
        return self.certification.title


class Oponency(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    date = models.DateField()
    element = GenericForeignKey('content_type', 'object_id') # Articulo, Tesis, Resultado, Proyecto
    opponents = GM2MField(Worker, ExternalPerson, related_name='oponencys')

    def __str__(self):
        return self.element.title


# Ok
class Tribunal(models.Model):
    date = models.DateField()
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    members = GM2MField(Worker, ExternalPerson, related_name='tribunals')

    def __str__(self):
        return self.thesis.title



