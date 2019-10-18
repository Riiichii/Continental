from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_index, name='index.html'),
    path('', views.post_formulario, name='formulario.html'),
]