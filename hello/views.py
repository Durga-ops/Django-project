from django.shortcuts import render
from django.http import HttpResponse

def intro(request):           #to return text
    return HttpResponse('Hi,This is Durga konda')
def intro1(request):       #to return data in html
    return render(request,'hi.html',{'name':'kiran'})
def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res= val1 + val2
    return render(request,'result.html',{'result':res})