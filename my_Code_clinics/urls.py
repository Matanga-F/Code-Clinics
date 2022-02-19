from django.urls import path
from . import views

app_name = "Code Clinics"

urlpatterns = [
    path("", views.index, name = "index"),
    path("sign/", views.sign, name="sign"),
]

