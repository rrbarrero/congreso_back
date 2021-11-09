from django.contrib import admin
from .models import Inscripcion


class InscripcionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellidos", "email", "telefono", "created_at")
    list_filter = (
        "estado_inscripcion",
        "jornada_experienciales",
        "sector_laboral",
        "terminada",
        "educativo_sector",
        "renuncia",
        "certificado",
        "created_at",
    )
    search_fields = ("nombre", "apellidos", "email", "telefono", "localidad")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)


admin.site.register(Inscripcion, InscripcionAdmin)
