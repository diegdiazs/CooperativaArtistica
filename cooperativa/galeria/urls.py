from django.urls import path
from .views import home
from .views import contacto
from .views import exposiciones
from .views import fotografia
from .views import iniciosesion
from .views import registro

urlpatterns = [
    path('',home,name='home'),
    path('/contacto',contacto,name='contacto'),
    path('/exposiciones',exposiciones,name='exposiciones'),
    path('/fotografia',fotografia,name='fotografia'),
    path('/iniciosesion',iniciosesion,name='iniciosesion'),
    path('/registro',registro,name='registro'),

]