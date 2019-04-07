from django.shortcuts import render
from django.http import HttpResponse
from .models import Reg
from .forms import LoginForm
from .forms import RegForm
from .forms import LocationForm
from .forms import PaymentForm
def reg(request):
        if request.method == 'POST':
                form = RegForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponse('reg success')
                else:
                        print(form.errors)
                        return HttpResponse("error")
        else:
                form = RegForm()
                return render(request,'reg.html',{'form': form})
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            un =form.cleaned_data['username']
            pw =form.cleaned_data['pwd']
            dbuser = Reg.objects.filter(username=un,
                                        pwd=pw)
            if not dbuser:
                return HttpResponse('login faild')
            else:
                return HttpResponse('login success')
    else:
        form = LoginForm()
        return render(request, 'login.html'
                      , {'form': form})
def location(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            State =form.cleaned_data['State']
            Mandal=form.cleaned_data['Mandal']
            Village=form.cleaned_data['Village']
    else:
        form = LocationForm()
        return render(request, 'location.html'
                      , {'form': form})
def payment(request):
        if request.method == "POST":
                form = PaymentForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponse('Payment success')
                else:
                        print(form.errors)
                        return HttpResponse("error")
        else:
                form = PaymentForm()
                return render(request, 'payment.html',{'form': form})
def home(request):
    return render(request,'home.html')





