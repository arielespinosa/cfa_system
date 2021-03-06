# Generated by Django 2.2.5 on 2021-05-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=50)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
