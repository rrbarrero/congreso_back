import factory
from faker import Faker
from .models import Inscripcion

fake = Faker("es_ES")


class InscripcionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Inscripcion

    nombre = factory.Faker("name")
    apellidos = factory.Faker("name")
    email = factory.Faker("email")
    telefono = fake.bothify(text="#########")
    localidad = fake.city()
    edad = fake.random_int(min=18, max=60)
    dni = factory.Sequence(lambda n: f"931232{n}-S")
    localidad_trabajo = fake.city()
    sexo = fake.random_element(("V", "M"))
    sector_laboral = fake.random_element(
        elements=([x[0] for x in Inscripcion.SITUACION_LABORAL_CHOICES])
    )
    conoce_lsa = fake.boolean()
    participado_accion_lsa = fake.boolean()
    asistido_congreso_uno = fake.boolean()
    asistido_congreso_dos = fake.boolean()
    asistido_congreso_tres = fake.boolean()
    conoce_eslogan_congreso_tres = fake.boolean()
    conoce_eslogan_congreso_tres_detalle = fake.sentence(nb_words=6)
    conoce_comunidad_lsa = fake.boolean()
    registrado_comunidad_lsa = fake.boolean()
    aplicado_conocimientos = fake.boolean()
    aplicado_conocimientos_detalle = fake.sentence(nb_words=6)
    jornada_experienciales = fake.random_element(
        elements=([x[0] for x in Inscripcion.JORNADA_EXP_CHOICES])
    )
    compromiso = fake.sentence(nb_words=6)
    proximo_anio = fake.text()
    proyectos = fake.text()
    desplegar_aprendido = fake.text()
    competencias_clave_eleccion = fake.text()

    @factory.lazy_attribute
    def educativo_sector(self):
        if self.sector_laboral == "SE":
            return fake.random_element(
                elements=([x[0] for x in Inscripcion.EDUCATIVO_CHOICES[1:]])
            )
        return ""

    @factory.lazy_attribute
    def funcionario_sector(self):
        if self.sector_laboral == "FP":
            return fake.sentence(nb_words=3)
        return ""

    @factory.lazy_attribute
    def trabajador_cuenta_ajena_sector(self):
        if self.sector_laboral == "CA":
            return fake.sentence(nb_words=3)
        return ""

    @factory.lazy_attribute
    def empresario_sector(self):
        if self.sector_laboral == "EA":
            return fake.sentence(nb_words=3)
        return ""

    @factory.lazy_attribute
    def emprendedor_sector(self):
        if self.sector_laboral == "E":
            return fake.sentence(nb_words=3)
        return ""

    @factory.lazy_attribute
    def ong_sector(self):
        if self.sector_laboral == "O":
            return fake.sentence(nb_words=3)
        return ""

    @factory.lazy_attribute
    def estudiante_especialidad(self):
        if self.sector_laboral == "ES":
            return fake.sentence(nb_words=3)
        return ""

    @factory.lazy_attribute
    def otro_area_laboral(self):
        if self.sector_laboral == "OL":
            return fake.sentence()
        return ""
