# Generated by Django 3.2.9 on 2021-11-24 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0013_alter_inscripcion_educativo_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='estado_inscripcion',
            field=models.CharField(choices=[('P', 'Pendiente'), ('A', 'Admitida'), ('R', 'En reserva'), ('D', 'Denegada')], default='P', max_length=1, verbose_name='Estado'),
        ),
    ]