# Generated by Django 3.2.9 on 2021-11-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0012_inscripcion_en_plazo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='educativo_sector',
            field=models.CharField(blank=True, choices=[('', ''), ('UN', 'Universitario'), ('BA', 'Bachillerato'), ('ES', 'ESO'), ('FP', 'FP'), ('CF', 'Ciclos Formativos'), ('PI', 'Primaria Infantil')], default='', max_length=2, verbose_name='Sector Educativo'),
        ),
    ]
