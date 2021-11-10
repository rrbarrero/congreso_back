import json
import factory
import pytest
from django.test import Client
from django.urls import reverse
from inscripciones.models import Inscripcion
from inscripciones.factory import InscripcionFactory
from mailapp.models import Plantilla


@pytest.fixture(autouse=True)
def create_mail_template():
    Plantilla.objects.create(
        nombre="registro ok",
        identificador="registro-ok",
        asunto="Asunto Registro ok",
        body_content="body mail registro ok",
    )
    assert Plantilla.objects.count() == 1


@pytest.mark.django_db
def test_new_sign_up():
    browser = Client()
    inscripcion = factory.build(dict, FACTORY_CLASS=InscripcionFactory)
    inscripcion["email2"] = inscripcion["email"]
    response = browser.post(
        reverse("signup"), json.dumps(inscripcion), content_type="application/json"
    )
    assert response.status_code == 200
    assert response.content == b'{"status": "ok"}'
