from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.
from django.http import HttpResponse

from .forms import MainForm1
from .import identifier as id

def Welcome(request):
    return render(request,'welcome.html')

def home(request):
    return render(request,'home.html')

def forget(request):
    return HttpResponse("Done")

def welcomer(request):
    return render(request,'home.html')

def expression(request):

    my_form = MainForm1()
    if request.method =='POST':
     my_form =MainForm1(request.POST)
     context1=""
     con=""

     if my_form.is_valid():
         result=request.POST.get('code')
         if result ==None:
             print(type(result))
         else:
             print("ok")
             print("result")
             print("result type",type(result))
             op=id.bag_of_words(result)
             print(op)
             context1=id.function2(op)
             con=id.function1()

         print(my_form.cleaned_data)

     else:
         print(my_form.errors)

     c={
        'form':my_form,
         "context":context1,

         "accuracy":con
       }
     return render(request,'home.html',c)

def blogin(request):
      return  render(request,'login.html')

