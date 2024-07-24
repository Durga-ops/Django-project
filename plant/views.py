from django.shortcuts import render
from django.http import HttpResponse
from .models import Placce

def index(request):
    plc1=Placce()
    plc1.name="Red Flower"
    plc1.price=40
    plc1.img='9.jpg' 
    plc1.hot=True
    
    plc2=Placce()
    plc2.name="Blue Flower"
    plc2.price=50
    plc2.img='10.jpg'
    plc2.hot=False


    plc3=Placce()
    plc3.name="Orange Flower"
    plc3.price=60
    plc3.img='11.jpg'
    plc3.hot=True


    plc4=Placce()
    plc4.name="Pink Flower"
    plc4.price=70
    plc4.img='12.jpg'
    plc4.hot=False


    plcs=[plc1,plc2,plc3,plc4]
    return render (request,'index.html',{'plcs':plcs})

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def portfolio(request):
    return render(request,'portfolio.html')
def single_portfolio(request):
    return render(request,'single_portfolio.html')
