from django.urls import path
from appfinancial.views import *


urlpatterns = [
    path("inicio",inicio, name="financial-inicio"),
    path("crypto/",crypto,name="financial-crypto"),
    path("raices/",raices, name="financial-raices"),
    path("activos/",activos,name="financial-activos"),
]

