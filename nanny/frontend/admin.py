from django.contrib import admin

# Register your models here.
from .models import Patient, VaccineManufacturer, VaccineShipment, VaccineDose

admin.site.register(Patient)
admin.site.register(VaccineManufacturer)
admin.site.register(VaccineShipment)
admin.site.register(VaccineDose)
