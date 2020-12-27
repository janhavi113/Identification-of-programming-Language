from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def forgot(request):
    username1 = request.POST.get('x1')
    pass1=  request.POST.get('x2')
    pass2= request.POST.get('x3')
    if pass1==pass2:
        p="yes"
    else:
        p="no"



    return render(request,'forgot.html',{'rr':username1,'pp':p})