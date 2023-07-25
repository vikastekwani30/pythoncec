from django.shortcuts import render

# Create your views here.
def Hello(request):
    return render(request,'home.html')

def India(request):
    return render(request,'india.html')
def Gujarat(request):
    return render(request,'guj.html')
def Maharastra(request):
    return render(request,'maha.html')
def Karanataka(request):
    return render(request,'kar.html')

def Gandhi(request):
    return render(request,'gandhi.html')

def Mumbai(request):
    return render(request,'mum.html')

def Bengaluru(request):
    return render(request,'beng.html')

def Australia(request):
    return render(request,'aus.html')

def America(request):
    return render(request,'america.html')

def California(request):
    return render(request,'cal.html')
def Florida(request):
    return render(request,'florida.html')
def Geo(request):
    return render(request,'geo.html')


