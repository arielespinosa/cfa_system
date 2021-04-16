from piloto.app_models.workers import ExternalPerson, Worker
from piloto.app_models.science import (Thesis, Article, Result, Project, Book)
from piloto.app_models.nomenclators import WorkField
from piloto.app_models.docent import CourseEdition


def all_persons_choices(pworker=None):
    if pworker:
        choices = [(worker.pk, '{0} {1} {2}'.format(worker.name, worker.lastname1, worker.lastname2)) for worker in Worker.objects.all().exclude(pk=pworker.pk)]
    else:
        choices = [(worker.pk, '{0} {1} {2}'.format(worker.name, worker.lastname1, worker.lastname2)) for worker in Worker.objects.all()]
    choices += [(person.pk, '{0} {1} {2}'.format(person.name, person.lastname1, person.lastname2)) for person in ExternalPerson.objects.all()]
    return choices


def scientific_elements_choices():
    elements = list()
    elements.extend(list(Thesis.objects.all()))
    elements.extend(list(Article.objects.all()))
    elements.extend(list(Result.objects.all()))
    elements.extend(list(Project.objects.all()))
    elements.extend(list(Book.objects.all()))
    return [(element.pk, '{0}: {1}'.format(element.type, element.title)) for element in elements]


def courses_choices(pworker=None):
    if pworker:
        choices = [(course.pk, 'Edición {0}: {1}'.format(course.edicion, course)) for course in CourseEdition.objects.all()] # .exclude(estudiantes__pk=trabajador.pk)
    else:
        pass
    return choices


def work_field_choices():
    return [(work_field.pk, '{0}. en {1}'.format(work_field.category, work_field.field)) for work_field in WorkField.objects.all()]
