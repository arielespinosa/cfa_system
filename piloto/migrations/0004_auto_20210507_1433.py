# Generated by Django 2.2.5 on 2021-05-07 14:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('piloto', '0003_auto_20210507_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.ImageField(default='default.jpg', null=True, upload_to='user_avatar/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='aproved_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 7, 14, 33, 35, 209983)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 7, 14, 33, 35, 210008)),
        ),
        migrations.AlterField(
            model_name='service',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 7, 14, 33, 35, 225665, tzinfo=utc)),
        ),
    ]
