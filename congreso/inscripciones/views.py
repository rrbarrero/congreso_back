import json
from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from inscripciones.models import Inscripcion
from django.core.validators import validate_email
from mailapp.models import Plantilla
from mailapp.utils import sendCustomMail


def Csrf(request):
    return JsonResponse({"csrfToken": get_token(request)})


def Sign_up(request):
    if request.method == "POST":
        dataForm = json.loads(request.body)
        dataForm.pop("email2")
        inscripcion = Inscripcion(**dataForm)
        inscripcion.save()
        if inscripcion.fecha_inscripcion_comunidad_lsa:
            if inscripcion.en_plazo:
                mailTemplate = Plantilla.objects.get(nombre="pendiente")
                sendCustomMail(mailTemplate, inscripcion)
                return JsonResponse({"status": "recibida"})
            mailTemplate = Plantilla.objects.get(nombre="reserva")
            sendCustomMail(mailTemplate, inscripcion)
            return JsonResponse({"status": "reserva"})
        mailTemplate = Plantilla.objects.get(nombre="denegada")
        sendCustomMail(mailTemplate, inscripcion)
        return JsonResponse({"status": "denegada"})
    return JsonResponse({"status": "error"})


def Check_mail(request, email):
    try:
        validate_email(email)
        if Inscripcion.objects.filter(email=email).count() > 0:
            return JsonResponse({"status": "error"})
        return JsonResponse({"status": "ok"})
    except:
        return JsonResponse({"status": "error"})
