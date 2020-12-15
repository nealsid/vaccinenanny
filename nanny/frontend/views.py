from django.shortcuts import render, get_object_or_404
from .models import Patient, VaccineDose
from django.utils import timezone

# Create your views here
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    doses = VaccineDose.objects.filter(patient = patient).order_by('-date_given')

    # see if patient has only received 1 vaccine and we're approaching
    # a few days before they need the second dose
    singleDose = len(doses) == 1
    doubleDose = len(doses) == 2

    if singleDose:
        last_dose_date = doses[0].date_given
        n = timezone.now()
        days_since_last_vaccine = (n - last_dose_date).days
    elif doubleDose:
        last_dose_date = doses[0].date_given
        days_since_last_vaccine = (timezone.now() - last_dose_date).days
        days_between_doses = (doses[0].date_given - doses[1].date_given).days
    else:
        days_since_last_vaccine = 'never'

    second_dose_warning = (singleDose and days_since_last_vaccine > 20)

    return render(request, 'frontend/patient.html', {'patient': patient,
                                                     'doses' : doses,
                                                     'days_since_last_vaccine': days_since_last_vaccine,
                                                     'second_dose_warning' : second_dose_warning,
                                                     'both_doses' : doubleDose})

# def patients_within_missing_dose_threshold(request):
#     patients_and_dose_count = VaccineDose.objects.values('patient').annotate(Count('patient'))
#     # TODO filter out patients with >1 dose in query
#     patients_with_one_dose = []
#     for pd in patients_and_dose_count:
#         if pd.patient_count == 1:
