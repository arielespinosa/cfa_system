# Generated by Django 2.2.5 on 2021-05-07 13:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import gm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('institutional_email', models.EmailField(max_length=254)),
                ('home_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('institutional_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('institutional_cellphone', models.CharField(blank=True, max_length=20, null=True)),
                ('private_cellphone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(default='Cuba', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='KnowledgeField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('older_group', models.CharField(blank=True, choices=[('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII'), ('IX', 'IX'), ('X', 'X'), ('XI', 'XI'), ('XII', 'XII'), ('XIII', 'XIII'), ('XIV', 'XIV'), ('XV', 'XV'), ('XVI', 'XVI'), ('XVII', 'XVII'), ('XVIII', 'XVIII'), ('XIX', 'XIX'), ('XX', 'XX'), ('XXI', 'XXI'), ('XXII', 'XXII'), ('XXIII', 'XXIII'), ('XXIV', 'XXIV'), ('XXV', 'XXV')], max_length=10, null=True)),
                ('current_group', models.CharField(choices=[('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII'), ('IX', 'IX'), ('X', 'X'), ('XI', 'XI'), ('XII', 'XII'), ('XIII', 'XIII'), ('XIV', 'XIV'), ('XV', 'XV'), ('XVI', 'XVI'), ('XVII', 'XVII'), ('XVIII', 'XVIII'), ('XIX', 'XIX'), ('XX', 'XX'), ('XXI', 'XXI'), ('XXII', 'XXII'), ('XXIII', 'XXIII'), ('XXIV', 'XXIV'), ('XXV', 'XXV')], max_length=10)),
                ('older_salary', models.FloatField(blank=True, null=True)),
                ('current_salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeopleOrganism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(default='22222222222', max_length=11, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('lastname1', models.CharField(max_length=50)),
                ('lastname2', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=20)),
                ('scientific_grade', models.CharField(blank=True, choices=[('MSc', 'Master'), ('Dr', 'Doctor(a)')], max_length=50, null=True)),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='piloto.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PoliticOrganism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ponency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', gm2m.fields.GM2MField('piloto.Worker', 'piloto.ExternalPerson', related_name='ponencys', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(blank=True, choices=[('CITMA', 'Ministerio de Ciencia, Tecnología y Medio Ambiente'), ('ACC', 'Academia de Ciencias'), ('MES', 'Ministerio de Educación Superior'), ('O', 'Otro')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ScienceElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudyCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(default='Cuba', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('scienceelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='piloto.ScienceElement')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('manager_by_cfa', models.BooleanField(default=True)),
                ('approved_by_cc', models.BooleanField(default=False)),
                ('level', models.CharField(choices=[('1', 'Primer Nivel'), ('2', 'Segundo Nivel'), ('3', 'Tercer Nivel')], max_length=40)),
                ('integrants', gm2m.fields.GM2MField('piloto.Worker', 'piloto.ExternalPerson', related_name='results', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
                ('prize', models.ManyToManyField(blank=True, null=True, to='piloto.Prize')),
            ],
            bases=('piloto.scienceelement',),
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('scienceelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='piloto.ScienceElement')),
                ('object_id', models.PositiveIntegerField()),
                ('grade', models.CharField(choices=[('S', 'Superior'), ('MSc', 'Master'), ('Dr', 'Doctorado')], max_length=10)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('end_date_tutor', models.DateField(blank=True, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Field')),
                ('study_center', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.StudyCenter')),
                ('tutors', gm2m.fields.GM2MField('piloto.Worker', 'piloto.ExternalPerson', related_name='thesis_tutoradas', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
            ],
            bases=('piloto.scienceelement',),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='piloto.Person')),
                ('avatar', models.ImageField(default='avatar_default.jpg', null=True, upload_to='fotos_de_perfiles/')),
                ('skin_color', models.CharField(choices=[('B', 'Blanca'), ('M', 'Mestiza'), ('N', 'Negra')], max_length=20)),
                ('scholar_lvl', models.CharField(choices=[('M', 'Medio'), ('S', 'Superior')], max_length=50)),
                ('scientific_category', models.CharField(blank=True, choices=[('AI', 'Aspirante a Investigador'), ('IA', 'Investigador Agregado'), ('IT', 'Investigador Titular')], max_length=50, null=True)),
                ('docent_category', models.CharField(blank=True, choices=[('PI', 'Profesor Instructor'), ('PS', 'Profesor Asistente'), ('PX', 'Profesor Auxiliar'), ('PA', 'Profesor Agregado'), ('PT', 'Profesor Titular')], max_length=50, null=True)),
                ('card', models.IntegerField(unique=True)),
                ('work_category', models.CharField(choices=[('T', 'Técnico'), ('E', 'Especialista')], max_length=20)),
                ('in_insmet_date', models.DateField(default=django.utils.timezone.now)),
                ('out_insmet_date', models.DateField(blank=True, null=True)),
                ('out_motivations', models.TextField(blank=True, max_length=1000, null=True)),
                ('res_34_19', models.FloatField(blank=True, null=True)),
                ('msc_dr', models.FloatField(blank=True, null=True)),
                ('other_old_payments', models.FloatField(blank=True, null=True)),
                ('other_current_payments', models.FloatField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('app_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('areas_of_interest', models.ManyToManyField(blank=True, null=True, to='piloto.KnowledgeField')),
                ('municipality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Municipality')),
                ('ocupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Occupation')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Office')),
                ('people_organisms', models.ManyToManyField(blank=True, null=True, to='piloto.PeopleOrganism')),
                ('politics_organisms', models.ManyToManyField(blank=True, null=True, to='piloto.PoliticOrganism')),
            ],
            bases=('piloto.person',),
        ),
        migrations.CreateModel(
            name='WorkField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Téc', 'Técnico'), ('Ing', 'Ingeniero'), ('Lic', 'Licenciado')], max_length=50)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Field')),
                ('study_center', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.StudyCenter')),
            ],
        ),
        migrations.CreateModel(
            name='SciencePrize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('prize', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Prize')),
            ],
        ),
        migrations.CreateModel(
            name='Oponency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('opponents', gm2m.fields.GM2MField('piloto.Worker', 'piloto.ExternalPerson', related_name='oponencys', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=500)),
                ('level', models.CharField(choices=[('N', 'Nacional'), ('I', 'Internacional')], max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('hours', models.FloatField()),
                ('credits', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('certification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Certification')),
                ('study_center', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.StudyCenter')),
            ],
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField()),
                ('integrants', gm2m.fields.GM2MField('piloto.Worker', 'piloto.ExternalPerson', related_name='comisiones', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
            ],
        ),
        migrations.CreateModel(
            name='WorkerCertification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('certification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Certification')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='certifications', to='piloto.Worker')),
            ],
        ),
        migrations.AddField(
            model_name='worker',
            name='work_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.WorkField'),
        ),
        migrations.CreateModel(
            name='Tribunal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('members', gm2m.fields.GM2MField('piloto.Worker', 'piloto.ExternalPerson', related_name='tribunals', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
                ('thesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piloto.Thesis')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('start_date', models.DateField(default=datetime.datetime(2021, 5, 7, 13, 48, 19, 539702, tzinfo=utc))),
                ('end_date', models.DateField()),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('type_of', models.CharField(blank=True, choices=[('EST', 'Estatal'), ('COM', 'Comercial'), ('EXP', 'Exportación')], max_length=20, null=True)),
                ('dim', models.CharField(blank=True, max_length=50, null=True)),
                ('mont', models.FloatField(default=0.0)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='piloto.Client')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('cost_center', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.CostCenter')),
                ('entity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='piloto.Entity')),
                ('participants', gm2m.fields.GM2MField('piloto.Worker', 'piloto.ExternalPerson', related_name='services', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
                ('tasks', models.ManyToManyField(blank=True, null=True, to='piloto.Task')),
                ('results', models.ManyToManyField(blank=True, null=True, to='piloto.Result')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('scienceelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='piloto.ScienceElement')),
                ('object_id', models.PositiveIntegerField()),
                ('manager_by_cfa', models.BooleanField(default=False)),
                ('level', models.CharField(blank=True, choices=[('PP', 'Programa Priorizado'), ('PE', 'Proyecto Empresarial'), ('INF', 'Institucional ft'), ('IN', 'Institucional')], max_length=40, null=True)),
                ('aproved_date', models.DateField(default=datetime.datetime(2021, 5, 7, 13, 48, 19, 522607))),
                ('start_date', models.DateField(default=datetime.datetime(2021, 5, 7, 13, 48, 19, 522634))),
                ('end_plan_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('cost_center', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.CostCenter')),
                ('entity', models.ManyToManyField(blank=True, null=True, related_name='entities', to='piloto.Entity')),
                ('executor_entity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Entity')),
                ('participants', gm2m.fields.GM2MField('piloto.Worker', 'piloto.ExternalPerson', related_name='projects', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Program')),
                ('results', models.ManyToManyField(blank=True, null=True, to='piloto.Result')),
            ],
            bases=('piloto.scienceelement',),
        ),
        migrations.CreateModel(
            name='PonencyRealized',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participation', models.CharField(choices=[('API_CO', 'Autor Principal Invitado por CO'), ('PAP', 'Ponente Autor Principal'), ('P', 'Ponente')], max_length=40)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Event')),
                ('ponency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='editions', to='piloto.Ponency')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Worker')),
            ],
        ),
        migrations.CreateModel(
            name='ExternalPerson',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='piloto.Person')),
                ('app_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('piloto.person',),
        ),
        migrations.CreateModel(
            name='CourseEdition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('edition', models.PositiveSmallIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piloto.Course')),
                ('students', models.ManyToManyField(related_name='courses', to='piloto.Worker')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('scienceelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='piloto.ScienceElement')),
                ('isbn', models.CharField(max_length=50)),
                ('data_base', models.CharField(blank=True, max_length=100, null=True)),
                ('pages', models.CharField(max_length=50)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('web_url', models.URLField(blank=True, null=True)),
                ('editorial', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('chapter', models.CharField(max_length=50)),
                ('total_pages', models.CharField(max_length=50)),
                ('gray_literature', models.BooleanField(default=False)),
                ('authors', gm2m.fields.GM2MField('piloto.Worker', 'piloto.ExternalPerson', related_name='books', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
            ],
            bases=('piloto.scienceelement',),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('scienceelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='piloto.ScienceElement')),
                ('doi', models.CharField(max_length=50, unique=True)),
                ('database', models.CharField(blank=True, max_length=100, null=True)),
                ('pages', models.CharField(max_length=50)),
                ('pub_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('web_url', models.URLField(blank=True, null=True)),
                ('magazine', models.CharField(blank=True, max_length=200, null=True)),
                ('issn', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('volume', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('impact_level', models.CharField(blank=True, choices=[('I', 'Grupo I'), ('II', 'Grupo II'), ('III', 'Grupo III'), ('IV', 'Grupo IV')], max_length=50, null=True)),
                ('participation', models.CharField(choices=[('AP', 'Autor Principal'), ('OA', 'Otro Autor')], max_length=50)),
                ('indexed', models.BooleanField(default=False)),
                ('refereed', models.BooleanField(default=False)),
                ('gray_literature', models.BooleanField(default=False)),
                ('authors', gm2m.fields.GM2MField('piloto.Worker', 'piloto.ExternalPerson', related_name='articles', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
            ],
            bases=('piloto.scienceelement',),
        ),
    ]
