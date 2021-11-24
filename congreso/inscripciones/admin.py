from django.contrib import admin
from .models import Inscripcion
from mailapp.utils import sendCustomMail
from mailapp.models import Plantilla


class InscripcionAdmin(admin.ModelAdmin):
    actions = [
        "confirmar_y_concluir",
    ]
    list_display = (
        "nombre",
        "apellidos",
        "email",
        "telefono",
        "estado_inscripcion",
        "created_at",
    )
    list_filter = (
        "estado_inscripcion",
        "jornada_experienciales",
        "sector_laboral",
        "terminada",
        "educativo_sector",
        "renuncia",
        "certificado",
        "sexo",
        "created_at",
    )
    search_fields = ("nombre", "apellidos", "email", "telefono", "localidad")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    def confirmar_y_concluir(self, request, queryset):
        queryset.update(estado_inscripcion=Inscripcion.ADMITIDA, terminada=True)
        plantilla = Plantilla.objects.get(identificador="notificacion-admitido")
        for inscripcion in queryset:
            sendCustomMail(plantilla, inscripcion)

    confirmar_y_concluir.short_description = (
        "Confirmar, notificar y concluir inscripciones"
    )


admin.site.register(Inscripcion, InscripcionAdmin)
