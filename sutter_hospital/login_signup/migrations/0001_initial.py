# Generated by Django 3.2.5 on 2021-07-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=10)),
                ('dob', models.DateField()),
                ('disease', models.CharField(max_length=30)),
                ('r_person', models.CharField(max_length=20)),
                ('profile_photo', models.ImageField()),
            ],
        ),
    ]