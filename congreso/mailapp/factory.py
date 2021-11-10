import factory
from faker import Faker
from django.utils.text import slugify
from .models import Plantilla

fake = Faker("es_ES")

class PlantillaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Plantilla
    nombre = fake.text()
    asunto = fake.text()
    body_content = fake.text()

   @factory.lazy_attribute
    def identificador(self):
        return slugify(self.nombre)