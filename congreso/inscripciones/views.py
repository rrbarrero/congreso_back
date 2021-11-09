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
    if request == "POST":
        dataForm = json.loads(request.body.decode("utf-8"))
        dataForm.pop("email2")
        inscripcion = Inscripcion(**dataForm)
        inscripcion.save()
        if (
            Inscripcion.objects.filter(estado_inscripcion=Inscripcion.ACEPTADA).count()
            >= Inscripcion.AFORO
        ):
            mailTemplate = Plantilla.objects.get(identificador="registro-full")
            mailTemplate(mailTemplate, inscripcion)
            sendCustomMail(mailTemplate, inscripcion)
            return JsonResponse({"status": "ok_but_full"})
        mailTemplate = Plantilla.objects.get(identificador="registro-ok")
        sendCustomMail(mailTemplate, inscripcion)
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "error"})


def Check_mail(request, email):
    try:
        validate_email(email)
        if Inscripcion.objects.filter(email=email).count() > 0:
            return JsonResponse({"status": "error"})
        return JsonResponse({"status": "ok"})
    except:
        return JsonResponse({"status": "error"})
