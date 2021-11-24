from django.conf import settings
from datetime import datetime
import requests


def get_comunidadlsa_joined_at(email):
    URL = f"https://comunidadlsa.es/v1/usuarios/search/?email={email}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token {settings.CLSA_ADMIN_TOKEN}",
    }
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data["count"] == 1:
            date_joined = data["results"][0]["date_joined"]
            return datetime.strptime(date_joined, "%Y-%m-%dT%H:%M")
    return None
