from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect



def login(request):

    return render(request,'login.html')

def login1(request):
    if request.method == 'POST':
        username1=request.POST['i1']
        password=request.POST['i2']


        #print(student.objects.all())

        return redirect('http://127.0.0.1:8000/')


