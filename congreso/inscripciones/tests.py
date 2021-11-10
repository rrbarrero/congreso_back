import json
import factory
import pytest
from django.test import Client
from inscripciones.models import Inscripcion
from inscripciones.factory import InscripcionFactory


@pytest.mark.django_db
def test_new_sign_up():
    browser = Client()
    inscripcion = factory.build(dict, FACTORY_CLASS=InscripcionFactory)
    inscripcion["email2"] = inscripcion["email"]
    response = browser.post(
        "/api/v1/form/", json.dumps(inscripcion), content_type="application/json"
    )
    assert response.status_code == 200
    assert response.content == b"{'status': 'ok'}"
