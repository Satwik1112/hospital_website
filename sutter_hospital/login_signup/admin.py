from django.contrib import admin
from . models import UserData# add tables by writing here

# Register your models here.
# create class for view


class UserAdmin(admin.ModelAdmin):# for display proper information about entitites in admin panel
    list_display = ('name', 'password', 'address', 'contact', 'dob', 'r_person', 'disease')


# register new table by
admin.site.register(UserData, UserAdmin)# to access user table in admin panel
