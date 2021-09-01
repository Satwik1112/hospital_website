from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver  # add this
from django.db.models.signals import post_save


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medicine = models.CharField(max_length=20, default="as per doctor prescribed")

    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class UserData(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.IntegerField()
    dob = models.DateField()
    disease = models.CharField(max_length=30)
    r_person = models.CharField(max_length=20)
    profile_photo = models.ImageField()
