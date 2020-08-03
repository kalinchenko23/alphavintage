from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .apicall import InfoGatheringCompany
from .forms import Main,Aditinal1,Exchange_form


x=InfoGatheringCompany()

def data(request):
    form=Main()
    if request.method == 'POST':
        form = Main(request.POST)
        if form.is_valid():
            text=form.cleaned_data["company_name"]
    else:
        text=None

    context={
        'form':form,
        'data1':x.company_overview(text),
        'data2':x.income_statement(text),
        'data3':x.balanse_sheet(text),
        'data4':x.cash_flow(text)}


    return render(request,"alphavintage/company_info.html",context)

def crypto(request):
    form=Main()
    if request.method == 'POST':
        form = Main(request.POST)
        if form.is_valid():
            text=form.cleaned_data["company_name"]
    else:
        text=None
    context={"form":form,
            'data1':x.get_cryptocurrency_rate(text)}
    return render(request,"alphavintage/cryptocurrency.html",context)

def exchange_rate(request):
    form=Exchange_form()
    if request.method == 'POST':
        form = Exchange_form(request.POST)
        if form.is_valid():
            text1=form.cleaned_data["ex_from"]
            text2=form.cleaned_data["ex_to"]
    else:
        text1=None
        text2=None
    context={"form":form,
            'data1':x.get_currency_exchange_rate(text1,text2)}
    return render(request,"alphavintage/exchange_rate.html",context)



def stock(request):
    form=Main()
    if request.method == 'POST':
        form = Main(request.POST)
        if form.is_valid():
            text=form.cleaned_data["company_name"]
    else:
        text=None

    context={"form":form,
            'data1':x.get_daily_adjusted_stock(text)}
    return render(request,"alphavintage/stock_info.html",context)

def stock_history(request):

    form=Aditinal1()
    if request.method == 'POST':
        form= Aditinal1(request.POST)
        if form.is_valid():
            text1=form.cleaned_data["company_name"]
            text2=form.cleaned_data["year"]
    else:
        text1=None
        text2=None
    context={"form":form,
            'data1':x.get_daily_adjusted_stock_history(text1,text2)}
    return render(request,"alphavintage/stock_history.html",context)

def sector(request):
    context={"data":x.us_sector_performance()}
    return render(request,"alphavintage/sector.html",context)





def home(request):
    return render(request,"alphavintage/home.html")
def cp_search(request):
    form=Main()
    return render(request,"alphavintage/cp_search.html",{"form":form})













