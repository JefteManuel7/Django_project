# Generated by Django 4.2.6 on 2023-10-13 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fecha_creacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
