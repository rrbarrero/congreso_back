from django.contrib import admin
from excel_response import ExcelResponse
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from .models import Inscripcion
from mailapp.utils import sendCustomMail
from mailapp.models import Plantilla


class InscripcionAdmin(admin.ModelAdmin):
    actions = ["confirmar_y_concluir", "exportar", "mail_seleccionados"]
    list_display = (
        "nombre",
        "apellidos",
        "email",
        "telefono",
        "estado_inscripcion",
        "en_plazo",
        "created_at",
    )
    list_filter = (
        "en_plazo",
        "estado_inscripcion",
        "jornada_experienciales",
        "sector_laboral",
        "terminada",
        "educativo_sector",
        "renuncia",
        "certificado",
        "sexo",
        "fecha_inscripcion_comunidad_lsa",
        "created_at",
    )
    search_fields = ("nombre", "apellidos", "email", "telefono", "localidad")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    def confirmar_y_concluir(self, request, queryset):
        queryset.update(estado_inscripcion=Inscripcion.ADMITIDA, terminada=True)
        plantilla = Plantilla.objects.get(identificador="aceptado")
        for inscripcion in queryset:
            sendCustomMail(plantilla, inscripcion)

    confirmar_y_concluir.short_description = (
        "Confirmar, notificar y concluir inscripciones"
    )

    def exportar(self, request, queryset):
        data = [
            [
                "Nombre",
                "Apellidos",
                "Email",
                "Telf",
                "Localidad",
                "Edad",
                "dni",
                "Estado inscripción",
                "Concluído" "Fecha de inscripción",
            ]
        ]
        for inscripcion in queryset:
            concluido = "Sí" if inscripcion.terminada else "No"
            data.append(
                [
                    inscripcion.nombre,
                    inscripcion.apellidos,
                    inscripcion.email,
                    inscripcion.telefono,
                    inscripcion.localidad,
                    inscripcion.edad,
                    inscripcion.dni,
                    inscripcion.get_estado_inscripcion_display(),
                    concluido,
                    inscripcion.created_at,
                ]
            )
        return ExcelResponse(data)
        exportar.short_description = "Exportar inscripciones"

    def mail_seleccionados(self, request, queryset):
        selected = queryset.values_list("pk", flat=True)
        ct = ContentType.objects.get_for_model(queryset.model)
        return HttpResponseRedirect(
            "/sendmail/?ct=%s&ids=%s"
            % (
                ct.pk,
                ",".join(str(pk) for pk in selected),
            )
        )

    mail_seleccionados.short_description = "Enviar correo a selección"


admin.site.register(Inscripcion, InscripcionAdmin)
