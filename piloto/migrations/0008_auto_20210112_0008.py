# Generated by Django 2.2.5 on 2021-01-12 00:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import gm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('piloto', '0007_auto_20210111_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='integrants',
            field=gm2m.fields.GM2MField('piloto.Worker', 'piloto.ExternalPerson', related_name='results', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk')),
        ),
        migrations.AlterField(
            model_name='project',
            name='aproved_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 12, 0, 8, 36, 797289)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 12, 0, 8, 36, 797315)),
        ),
        migrations.AlterField(
            model_name='result',
            name='level',
            field=models.CharField(choices=[('1', 'Primer Nivel'), ('2', 'Segundo Nivel'), ('3', 'Tercer Nivel')], max_length=40),
        ),
        migrations.AlterField(
            model_name='service',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 12, 0, 8, 36, 812384, tzinfo=utc)),
        ),
    ]
