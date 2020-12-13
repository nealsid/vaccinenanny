from django.db import models

# Create your models here.

class Patient(models.Model):
    mrn = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

class VaccineManufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=50)
    vaccine_name = models.CharField(max_length=50)

class VaccineShipment(models.Model):
    vaccine = models.ForeignKey(VaccineManufacturer, on_delete=models.PROTECT)
    receive_date = models.DateTimeField('shipment received')
    doses = models.IntegerField()

class VaccineDose(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    date_given = models.DateTimeField('dose date')
