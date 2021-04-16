# Generated by Django 2.2.5 on 2021-04-07 00:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('piloto', '0013_auto_20210403_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='aproved_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 7, 0, 55, 36, 210905)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 7, 0, 55, 36, 210930)),
        ),
        migrations.AlterField(
            model_name='service',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 7, 0, 55, 36, 215441, tzinfo=utc)),
        ),
    ]