from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import UserData
import hashlib
# Create your views here.


def profile(request):
    userdata = UserData.objects.all()
    return render(request, 'homepage/profile.html', {'userdata': userdata})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        password = request.POST['password']
        address = request.POST['address']
        contact = request.POST['contact']
        dob = request.POST['dob']
        r_person = request.POST['r_person']
        disease = request.POST['disease']
        fl = name.split(' ')
        first_name = fl[0]
        last_name = fl[1]
        x = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
        password = bytes(password, 'utf-8')
        encrypted_password = hashlib.sha1(password).hexdigest()
        u = UserData(name=name, password=encrypted_password, address=address, contact=contact, dob=dob, r_person=r_person, disease=disease)#adds data to the table
        x.save()
        u.save()
        print('User is created for x', x)
        print('User is created for u', u)
        return redirect('/')
    else:
        return render(request, 'homepage/newadmit.html')

#user.name    user.dob


def user_login(request):
    if request.method == 'POST':
        users = User.objects.all()
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            print(user)
            print("login status", user.is_authenticated)
            return redirect('/')
        else:
            return render(request, 'homepage/oldadmit.html', {'error': 'Incorrect Details'})
    else:
        return render(request, 'homepage/oldadmit.html')


def user_logout(request):
    auth.logout(request)
    return redirect('/')
