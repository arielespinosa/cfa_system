from django.contrib import admin
from .app_models.workers import Worker, ExternalPerson
from .app_models.nomenclators import *
from .app_models.docent import *
from .app_models.science import *

# Worker
admin.site.register(Worker)
admin.site.register(ExternalPerson)

# Nomenclators
admin.site.register(Place)
admin.site.register(Contact)
admin.site.register(KnowledgeField)
admin.site.register(Municipality)
admin.site.register(Certification)
admin.site.register(Client)
admin.site.register(CostCenter)
admin.site.register(StudyCenter)
admin.site.register(Field)
admin.site.register(WorkField)
admin.site.register(Occupation)
admin.site.register(Office)
admin.site.register(PeopleOrganism)
admin.site.register(PoliticOrganism)
admin.site.register(Prize)
admin.site.register(Entity)
admin.site.register(Program)
admin.site.register(Task)

# Docent
admin.site.register(Course)
admin.site.register(CourseEdition)
admin.site.register(WorkerCertification)
admin.site.register(Event)
admin.site.register(Oponency)
admin.site.register(Ponency)
admin.site.register(PonencyRealized)
admin.site.register(Tribunal)
admin.site.register(Comision)

# Science
admin.site.register(Thesis)
admin.site.register(Article)
admin.site.register(Result)
admin.site.register(Project)
admin.site.register(Book)
admin.site.register(Service)
admin.site.register(SciencePrize)

