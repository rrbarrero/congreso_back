# Generated by Django 3.2.9 on 2021-11-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0006_auto_20211109_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcion',
            name='emprendedor_sector',
            field=models.CharField(blank=True, max_length=150, verbose_name='Sector Emprendedor'),
        ),
    ]
