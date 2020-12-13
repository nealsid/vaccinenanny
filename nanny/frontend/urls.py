from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient/<int:patient_id>', views.patient, name='patient'),
]
