from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'homepage/homepage.html')


def ourfacilities(request):
    return render(request, 'homepage/ourfacilities.html')


def about(request):
    return render(request, 'homepage/about.html')


def contactus(request):
    return render(request, 'homepage/contactus.html')

