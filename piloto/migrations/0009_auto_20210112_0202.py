# Generated by Django 2.2.5 on 2021-01-12 02:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('piloto', '0008_auto_20210112_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='aproved_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 12, 2, 2, 37, 829268)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 12, 2, 2, 37, 829298)),
        ),
        migrations.AlterField(
            model_name='scienceprize',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 12, 2, 2, 37, 845967, tzinfo=utc)),
        ),
    ]
