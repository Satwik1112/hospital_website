from django.shortcuts import render
from .models import Doctors
# Create your views here.


def doctors(request):
    doctors = Doctors.objects.all()
    return render(request, 'homepage/ourdoctors.html',
                  {'doctors': doctors})
