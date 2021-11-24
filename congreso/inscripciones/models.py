from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from .utils import get_comunidadlsa_joined_at


class Inscripcion(models.Model):

    AFORO = 400

    VACIO = ""
    ADMITIDA = "A"
    DENEGADA = "D"
    PENDIENTE = "P"
    ESTADOS_CHOICE = (
        (PENDIENTE, _("Pendiente")),
        (ADMITIDA, _("Admitida")),
        (DENEGADA, _("Denegada")),
    )
    UNIVERSITARIO = "UN"
    BACHILLERATO = "BA"
    ESO = "ES"
    FP = "FP"
    CICLOS_FORMATIVOS = "CF"
    PRIMARIA_INFANTIL = "PI"
    EDUCATIVO_CHOICES = (
        (VACIO, _("")),
        (UNIVERSITARIO, _("Universitario")),
        (BACHILLERATO, _("Bachillerato")),
        (ESO, _("ESO")),
        (FP, _("FP")),
        (CICLOS_FORMATIVOS, _("Ciclos Formativos")),
        (PRIMARIA_INFANTIL, _("Primaria Infantil")),
    )
    SECTOR_EDUCATIVO = "SE"
    FUNCIONARIO_PUBLICO = "FP"
    TRABAJADOR_POR_CUENTA_AJENA = "CA"
    EMPRESARIO_AUTONOMO = "EA"
    EMPRENDEDOR = "E"
    ONG = "O"
    DESEMPLEADO = "D"
    ESTUDIANTE = "ES"
    OTRA_SITUACION_LABORAL = "OL"
    SITUACION_LABORAL_CHOICES = (
        (TRABAJADOR_POR_CUENTA_AJENA, _("Trabajador por Cuenta Ajena")),
        (EMPRESARIO_AUTONOMO, _("Empresario/Autónomo")),
        (SECTOR_EDUCATIVO, _("Sector Educativo")),
        (FUNCIONARIO_PUBLICO, _("Funcionario Público")),
        (EMPRENDEDOR, _("Emprendedor")),
        (ONG, _("ONG")),
        (DESEMPLEADO, _("Desempleado")),
        (ESTUDIANTE, _("Estudiante")),
        (OTRA_SITUACION_LABORAL, _("Otra")),
    )
    JORNADA_EXP_EMPRENDEDORES = "JE"
    JORNADA_EXP_PADRES = "JP"
    JORNADA_EXP_DOCENTES = "JD"
    JORNADA_EXP_OTROS = "JO"
    JORNADA_EXP_CHOICES = (
        (JORNADA_EXP_EMPRENDEDORES, _("Jornada Emprendedores")),
        (JORNADA_EXP_PADRES, _("Jornada Padres")),
        (JORNADA_EXP_DOCENTES, _("Jornada Docentes")),
        (JORNADA_EXP_OTROS, _("Otros (estudiantes, profesionales, desempleados, etc.")),
    )
    VARON = "V"
    MUJER = "M"
    SEXO_CHOICES = (
        (VARON, _("Varón")),
        (MUJER, _("Mujer")),
    )

    nombre = models.CharField(_("Nombre"), max_length=150)
    apellidos = models.CharField(_("Apellidos"), max_length=150)
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    telefono = models.CharField(_("Teléfono"), max_length=9)
    localidad = models.CharField(_("Localidad"), max_length=150)
    edad = models.PositiveSmallIntegerField(_("Edad"))
    dni = models.CharField(_("DNI"), max_length=12, unique=True)
    localidad_trabajo = models.CharField(_("Localidad de trabajo"), max_length=150)
    sexo = models.CharField(
        _("Sexo"), max_length=1, choices=SEXO_CHOICES, default=MUJER
    )
    estado_inscripcion = models.CharField(
        _("Estado"), max_length=1, choices=ESTADOS_CHOICE, default=PENDIENTE
    )
    fecha_inscripcion_comunidad_lsa = models.DateField(
        _("Fecha de inscripción en la Comunidad LSA"), null=True, blank=True
    )
    en_plazo = models.BooleanField(_("En plazo"), default=False)
    terminada = models.BooleanField(_("Inscripción Concluida"), default=False)
    renuncia = models.BooleanField(_("Renuncia"), default=False)
    certificado = models.BooleanField(_("Reclama Certificado"), default=False)
    sector_laboral = models.CharField(
        _("Situación Laboral"),
        max_length=2,
        choices=SITUACION_LABORAL_CHOICES,
        default=TRABAJADOR_POR_CUENTA_AJENA,
    )
    educativo_sector = models.CharField(
        _("Sector Educativo"),
        max_length=2,
        choices=EDUCATIVO_CHOICES,
        default=VACIO,
    )
    funcionario_sector = models.CharField(
        _("Sector Funcionario"), max_length=150, blank=True
    )
    trabajador_cuenta_ajena_sector = models.CharField(
        _("Sector Cuenta Ajena"), max_length=150, blank=True
    )
    empresario_sector = models.CharField(
        _("Sector Empresario Autónomo"), max_length=150, blank=True
    )
    emprendedor_sector = models.CharField(
        _("Sector Emprendedor"), max_length=150, blank=True
    )
    ong_sector = models.CharField(_("Sector ONG"), max_length=150, blank=True)
    otro_area_laboral = models.CharField(_("Otro Sector"), max_length=150, blank=True)
    estudiante_especialidad = models.CharField(
        _("Estudiante Especialidad"), max_length=150, blank=True
    )
    conoce_lsa = models.BooleanField(_("Conoce LSA"), default=False)
    participado_accion_lsa = models.BooleanField(
        _("Participó en Acción LSA"), default=False
    )
    asistido_congreso_uno = models.BooleanField(_("Asistido Congreso 1"), default=False)
    asistido_congreso_dos = models.BooleanField(_("Asistido Congreso 2"), default=False)
    asistido_congreso_tres = models.BooleanField(
        _("Asistido Congreso 3"), default=False
    )
    conoce_eslogan_congreso_tres = models.BooleanField(
        _("Conoce Esloga Congreso 3"), default=False
    )
    conoce_eslogan_congreso_tres_detalle = models.CharField(
        _("Eslogan 3er Congreso"), max_length=150, blank=True
    )
    conoce_comunidad_lsa = models.BooleanField(_("Conoce Comunidad LSA"), default=False)
    registrado_comunidad_lsa = models.BooleanField(
        _("Registrado en Comunidad LSA"), default=False
    )
    aplicado_conocimientos = models.BooleanField(
        _("Aplicó conocimientos LSA"), default=False
    )
    aplicado_conocimientos_detalle = models.TextField(
        _("Detalle de Aplicación Conocimientos LSA"), blank=True
    )
    jornada_experienciales = models.CharField(
        _("Jornada Experiencial"),
        max_length=2,
        choices=JORNADA_EXP_CHOICES,
        default=JORNADA_EXP_EMPRENDEDORES,
    )
    compromiso = models.CharField(_("Compromiso"), max_length=150, blank=True)
    proximo_anio = models.TextField(
        _(
            "Qué estás dispuesto hacer el próximo año con todo lo aprendido en el marco de la Sociedad del Aprendizaje?"
        ),
    )
    proyectos = models.TextField(
        _("Tienes idea o proyectos para desarrollar o implementar en tu vida?"),
    )
    desplegar_aprendido = models.TextField(_("¿Cómo desplegarías lo aprendido?"))
    competencias_clave_eleccion = models.TextField(
        _(
            "¿Puedes decirnos, de las 10 competencias clave mencionadas en este documento, cuáles priorizarías para desarrollar más y aplicarlas en tu vida?"
        ),
    )
    created_at = models.DateTimeField(_("Fecha de inscripción"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Fecha de actualización"), auto_now=True)

    class Meta:
        verbose_name = _("Inscripción")
        verbose_name_plural = _("Inscripciones")

    def __str__(self):
        return self.email


@receiver(pre_save, sender=Inscripcion)
def _presave_receiver(sender, instance, *args, **kwargs):
    date_limit = datetime.strptime(settings.DATE_LIMIT, "%d/%m/%Y")
    joined_at = get_comunidadlsa_joined_at(instance.email)
    if joined_at:
        instance.fecha_inscripcion_comunidad_lsa = joined_at
        if joined_at <= date_limit:
            instance.en_plazo = True
