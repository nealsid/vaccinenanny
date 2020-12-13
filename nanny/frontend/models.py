from django.db import models

# Create your models here.

class Patient(models.Model):
    mrn = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

class VaccineManufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=50)
    vaccine_name = models.CharField(max_length=50)
    days_between_doses = models.IntegerField()

    def __str__(self):
        return self.manufacturer_name + ' ' + self.vaccine_name + '(' + str(self.days_between_doses) + ')'

class VaccineShipment(models.Model):
    vaccine = models.ForeignKey(VaccineManufacturer, on_delete=models.PROTECT)
    expected_receive_date = models.DateTimeField('expected receive date')
    received_date = models.DateTimeField('shipment received')
    doses = models.IntegerField()

class VaccineDose(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    vaccine = models.ForeignKey(VaccineManufacturer, on_delete=models.PROTECT, null=True)
    date_given = models.DateTimeField('dose date')
