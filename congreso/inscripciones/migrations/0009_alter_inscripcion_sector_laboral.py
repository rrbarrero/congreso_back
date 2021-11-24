# Generated by Django 3.2.9 on 2021-11-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0008_alter_inscripcion_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='sector_laboral',
            field=models.CharField(choices=[('CA', 'Trabajador por Cuenta Ajena'), ('EA', 'Empresario/Autónomo'), ('SE', 'Sector Educativo'), ('FP', 'Funcionario Público'), ('E', 'Emprendedor'), ('O', 'ONG'), ('D', 'Desempleado'), ('ES', 'Estudiante'), ('OL', 'Otra')], default='CA', max_length=2, verbose_name='Situación Laboral'),
        ),
    ]