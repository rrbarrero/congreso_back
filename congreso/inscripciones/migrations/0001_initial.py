# Generated by Django 3.2.9 on 2021-11-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('telefono', models.CharField(max_length=9, verbose_name='Teléfono')),
                ('localidad', models.CharField(max_length=150, verbose_name='Localidad')),
                ('edad', models.PositiveSmallIntegerField(verbose_name='Edad')),
                ('dni', models.CharField(max_length=9, unique=True, verbose_name='DNI')),
                ('localidad_trabajo', models.CharField(max_length=150, verbose_name='Localidad de trabajo')),
                ('mujer', models.BooleanField(default=False, verbose_name='Mujer')),
                ('varon', models.BooleanField(default=False, verbose_name='Varon')),
                ('estado_inscripcion', models.CharField(choices=[('P', 'Pendiente'), ('A', 'Admitida'), ('D', 'Denegada')], default='P', max_length=1, verbose_name='Estado')),
                ('terminada', models.BooleanField(default=False, verbose_name='Inscripción Concluida')),
                ('renuncia', models.BooleanField(default=False, verbose_name='Renuncia')),
                ('certificado', models.BooleanField(default=False, verbose_name='Reclama Certificado')),
                ('sector_lab', models.CharField(choices=[('', ''), ('CA', 'Trabajador por Cuenta Ajena'), ('EA', 'Empresario/Autónomo'), ('SE', 'Sector Educativo'), ('FP', 'Funcionario Público'), ('E', 'Emprendedor'), ('O', 'ONG'), ('D', 'Desempleado'), ('ES', 'Estudiante'), ('OL', 'Otra')], default='', max_length=2, verbose_name='Sector Laboral')),
                ('educativo_sector', models.CharField(choices=[('', ''), ('UN', 'Universitario'), ('BA', 'Bachillerato'), ('ES', 'ESO'), ('FP', 'FP'), ('CF', 'Ciclos Formativos'), ('PI', 'Primaria Infantil')], default='UN', max_length=2, verbose_name='Sector Educativo')),
                ('funcionario_sector', models.CharField(blank=True, max_length=150, verbose_name='Sector Funcionario')),
                ('trabajador_cuenta_ajena_sector', models.CharField(blank=True, max_length=150, verbose_name='Sector Cuenta Ajena')),
                ('empresario_sector', models.CharField(blank=True, max_length=150, verbose_name='Sector Empresario Autónomo')),
                ('ong_sector', models.CharField(blank=True, max_length=150, verbose_name='Sector ONG')),
                ('otro_area_laboral', models.CharField(blank=True, max_length=150, verbose_name='Otro Sector')),
                ('estudiante_especialidad', models.CharField(blank=True, max_length=150, verbose_name='Especialidad')),
                ('conoce_lsa', models.BooleanField(default=False, verbose_name='Conoce LSA')),
                ('participado_accion_lsa', models.BooleanField(default=False, verbose_name='Participó en Acción LSA')),
                ('asistido_congreso_uno', models.BooleanField(default=False, verbose_name='Asistido Congreso 1')),
                ('asistido_congreso_dos', models.BooleanField(default=False, verbose_name='Asistido Congreso 2')),
                ('asistido_congreso_tres', models.BooleanField(default=False, verbose_name='Asistido Congreso 3')),
                ('conoce_eslogan_congreso_tres', models.BooleanField(default=False, verbose_name='Conoce Esloga Congreso 3')),
                ('conoce_eslogan_congreso_tres_detalle', models.CharField(blank=True, max_length=150, verbose_name='Eslogan 3er Congreso')),
                ('conoce_comunidad_lsa', models.BooleanField(default=False, verbose_name='Conoce Comunidad LSA')),
                ('registrado_comunidad_lsa', models.BooleanField(default=False, verbose_name='Registrado en Comunidad LSA')),
                ('aplicado_conocimientos', models.BooleanField(default=False, verbose_name='Aplicó conocimientos LSA')),
                ('aplicado_conocimientos_detalle', models.TextField(blank=True, verbose_name='Detalle de Aplicación Conocimientos LSA')),
                ('jornada_experienciales', models.CharField(choices=[('JE', 'Jornada Emprendedores'), ('JP', 'Jornada Padres'), ('JD', 'Jornada Docentes'), ('JO', 'Otros (estudiantes, profesionales, desempleados, etc.')], default='JE', max_length=2, verbose_name='Jornada Experiencial')),
                ('compromiso', models.CharField(blank=True, max_length=150, verbose_name='Compromiso')),
                ('proximo_anio', models.CharField(max_length=200, verbose_name='Qué estás dispuesto hacer el próximo año con todo lo aprendido en el marco de la Sociedad del Aprendizaje?')),
                ('proyectos', models.CharField(max_length=250, verbose_name='Tienes idea o proyectos para desarrollar o implementar en tu vida?')),
                ('desplegar_aprendido', models.CharField(max_length=250, verbose_name='¿Cómo desplegarías lo aprendido?')),
                ('competencias_clave_eleccion', models.CharField(max_length=50, verbose_name='¿Puedes decirnos, de las 10 competencias clave mencionadas en este documento, cuáles priorizarías para desarrollar más y aplicarlas en tu vida?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]