from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),

    url(r'^list', views.events, name='list_events'), #listado
    url(r'^add/', views.add_event, name='add_event'), #formulario para añadir
    url(r'^(?P<eventid>\d+)/', views.update_event, name='update_event'), #formulario para editar
    url(r'^delete/(?P<eventid>\d+)/', views.delete_event, name='delete_event'), #ruta para eliminar

]