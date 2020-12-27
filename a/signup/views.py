

from django.shortcuts import render
from .models import student
# Create your views here.
from django.http import HttpResponse
def signup(request):
    print(request.method)
    if request.method == 'POST':
         username1 = request.POST.get('t1')
         pass1=  request.POST.get('t2')
         pass2= request.POST.get('t3')
         email=request.POST.get('t4')
         mob=request.POST.get('t5')
         s=student(username=username1,Password=pass1,Con_password=pass2,Email=email)
         s.save()

    return render(request,'signup.html')#,{'rr':username1,'pp':pass1,'pp2':pass2,'E':email,'M':mob})