from django.contrib import admin
from . models import Doctors# add tables by writing here

# Register your models here
# create class for view


class DoctorAdmin(admin.ModelAdmin):# for display proper information about entitites in admin panel
    list_display = ('name', 'specialization', 'contact', 'time', 'cabin')


# register new table by
admin.site.register(Doctors, DoctorAdmin)# to access user table in admin panel