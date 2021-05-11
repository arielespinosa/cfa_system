from django.urls import path
from .app_views import worker as view_worker
from .app_views import nomenclators as view_nomenclators
from .app_views import science as view_science
from .app_views import docent as view_docent
from .app_views import inventory as view_inventory
from .app_views import administration as view_administration
#from django_pdfkit import PDFView


app_name = 'piloto'

urlpatterns = [
    path('', view_worker.Index.as_view(), name='index'),

    # PERSONS
    path('external_person/create', view_worker.CreateExternalPerson.as_view(), name='create_external_person'),

    # NOMENCLATORS
    path('event/create', view_nomenclators.CreateEvent.as_view(), name='create_event'),
    path('certification/create', view_nomenclators.CreateCertificationView.as_view(), name='create_certification'),
    path('prize/create', view_nomenclators.CreatePrizeView.as_view(), name='create_prize'),
    path('entity/create', view_nomenclators.CreateEntity.as_view(), name='create_entity'),
    path('study_center/create', view_nomenclators.CreateStudyCenter.as_view(), name='create_study_center'),
    path('program/create', view_nomenclators.CreateProgram.as_view(), name='create_program'),
    path('client/create', view_nomenclators.CreateClient.as_view(), name='create_client'),
    path('cost_center/create', view_nomenclators.CreateCostCenter.as_view(), name='create_cost_center'),
    path('knowledge_field/create', view_nomenclators.CreateKnowledgeField.as_view(), name='create_knowledge_field'),
    path('field/create', view_nomenclators.CreateField.as_view(), name='create_field'),
    path('occupation/create', view_nomenclators.CreateOccupation.as_view(), name='create_occupation'),
    path('office/create', view_nomenclators.CreateOffice.as_view(), name='create_office'),
    path('people_organism/create', view_nomenclators.CreatePeopleOrganism.as_view(), name='create_people_organism'),
    path('politic_organism/create', view_nomenclators.CreatePoliticOrganism.as_view(), name='create_politic_organism'),
    path('task/create', view_nomenclators.CreateTask.as_view(), name='create_task'),

    # ADMINISTRATIVE WORK
    path('administration', view_administration.AdministrativeWorkView.as_view(), name='administration'),

    # Inventory
    path('inventory/create', view_inventory.CreateInventory.as_view(), name='create_inventory'),

    # SCIENCE
    # General
    path('science_work', view_science.WorkerScienceWorkView.as_view(), name='science_work'),

    # Create
    #path('oponency/create', view_science.CreateThesis.as_view(), name='create_oponency'),
    path('ponency/create', view_science.CreatePonency.as_view(), name='create_ponency'),
    path('ponency_realized/create', view_science.CreatePonencyRealized.as_view(), name='create_ponency_realized'),
    path('comision/create', view_science.CreateComision.as_view(), name='create_comision'),
    path('thesis/create', view_science.CreateThesis.as_view(), name='create_thesis'),
    path('service/create', view_science.CreateService.as_view(), name='create_service'),
    path('project/create', view_science.CreateProject.as_view(), name='create_project'),
    path('article/create', view_science.CreateArticle.as_view(), name='create_article'),
    path('book/create', view_science.CreateBook.as_view(), name='create_book'),
    path('result/create', view_science.CreateResult.as_view(), name='create_result'),
    path('science_prize/create', view_science.CreateSciencePrize.as_view(), name='create_science_prize'),

    # List
    path('ponencys/', view_science.ListPonency.as_view(), name='ponencys'),
    path('ponency_realized/', view_science.ListPonencyRealized.as_view(), name='ponency_realized'),
    path('comisions/', view_science.ListComision.as_view(), name='comisions'),
    path('thesis/', view_science.ListThesis.as_view(), name='thesis'),
    path('services/', view_science.ListService.as_view(), name='services'),
    path('projects/', view_science.ListProject.as_view(), name='projects'),
    path('articles/', view_science.ListArticles.as_view(), name='articles'),
    path('books/', view_science.ListBooks.as_view(), name='books'),
    path('results/', view_science.ListResults.as_view(), name='results'),
    path('science_prizes/', view_science.ListSciencePrize.as_view(), name='science_prizes'),

    # Delete
    path('ponencia/<int:pk>/eliminar/', view_science.DeletePonency.as_view(), name="delete_ponency"),
    path('ponencia_realizada/<int:pk>/eliminar/', view_science.DeletePonencyRealized.as_view(), name="delete_ponency_realized"),
    path('comision/<int:pk>/eliminar/', view_science.DeleteComision.as_view(), name="delete_comision"),
    path('tesis/<int:pk>/eliminar/', view_science.DeleteThesis.as_view(), name="delete_thesis"),
    path('servicio/<int:pk>/eliminar/', view_science.DeleteService.as_view(), name="delete_service"),
    path('proyecto/<int:pk>/eliminar/', view_science.DeleteProject.as_view(), name="delete_project"),
    path('articulo/<int:pk>/eliminar/', view_science.DeleteArticle.as_view(), name="delete_article"),
    path('libro/<int:pk>/eliminar/', view_science.DeleteBook.as_view(), name="delete_book"),
    path('resultado/<int:pk>/eliminar/', view_science.DeleteResult.as_view(), name="delete_result"),
    path('premio_cientifico/<int:pk>/eliminar/', view_science.DeleteSciencePrize.as_view(), name="delete_science_prize"),

    # DOCENT
    # General
    path('docent_work', view_docent.WorkerDocentWorkView.as_view(), name='docent_work'),

    # Create
    path('course/create', view_docent.CreateCourse.as_view(), name='create_course'),
    path('course_edition/create', view_docent.CreateCourseEdition.as_view(), name='create_course_edition'),
    path('tribunal/create', view_docent.CreateTribunal.as_view(), name='create_tribunal'),
    path('oponency/create', view_docent.CreateOponency.as_view(), name='create_oponency'),
    path('worker_certification/create', view_docent.CreateWorkerCertification.as_view(), name='create_worker_certification'),

    # List
    path('courses/', view_docent.ListCourse.as_view(), name='courses'),
    path('course_editions/', view_docent.ListCourseEdition.as_view(), name='course_editions'),
    path('tribunals/', view_docent.ListTribunal.as_view(), name='tribunals'),
    path('oponencys/', view_docent.ListOponency.as_view(), name='oponencys'),
    path('worker_certifications/', view_docent.ListWorkerCertification.as_view(), name='worker_certifications'),

    # Detail
    path('course/<int:pk>/', view_docent.DetailCourse.as_view(), name='detail_course'),
    path('course_edition/<int:pk>/', view_docent.DetailCourseEdition.as_view(), name='detail_course_edition'),
    path('tribunal/<int:pk>/', view_docent.DetailTribunal.as_view(), name='detail_tribunal'),
    path('oponency/<int:pk>/', view_docent.DetailOponency.as_view(), name='detail_oponency'),
    path('worker_certification/<int:pk>/', view_docent.DetailWorkerCertification.as_view(),
         name='detail_worker_certification'),

    # Update
    path('course/<int:pk>/update/', view_docent.UpdateCourse.as_view(), name='update_course'),
    path('course_edition/<int:pk>/update/', view_docent.UpdateCourseEdition.as_view(), name='update_course_edition'),
    path('tribunal/<int:pk>/update/', view_docent.UpdateTribunal.as_view(), name='update_tribunal'),
    path('oponency/<int:pk>/update/', view_docent.UpdateOponency.as_view(), name='update_oponency'),
    path('worker_certification/<int:pk>/update/', view_docent.UpdateWorkerCertification.as_view(),
         name='update_worker_certification'),

    # Delete
    path('course/<int:pk>/delete/', view_docent.DeleteCourse.as_view(), name='delete_course'),
    path('course_edition/<int:pk>/delete/', view_docent.DeleteCourseEdition.as_view(), name='delete_course_edition'),
    path('tribunal/<int:pk>/delete/', view_docent.DeleteTribunal.as_view(), name='delete_tribunal'),
    path('oponency/<int:pk>/delete/', view_docent.DeleteOponency.as_view(), name='delete_oponency'),
    path('worker_certification/<int:pk>/delete/', view_docent.DeleteWorkerCertification.as_view(),
         name='delete_worker_certification'),

]
