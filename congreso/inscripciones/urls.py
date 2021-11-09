from django.urls import path
from inscripciones import views

urlpatterns = [
    path("form/", views.Sign_up, name="signup"),
    path("csrf/", views.Csrf, name="csrf"),
    path("check_mail/<str:email>", views.Check_mail, name="check_mail"),
]
