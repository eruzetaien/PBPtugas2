import imp
from django.shortcuts import render
from mywatchlist.models import Watchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist = Watchlist.objects.all()
    counter_watched = 0
    for show in data_watchlist :
        if show.watched == True :
            counter_watched += 1
            
    if counter_watched >= len(data_watchlist):
        tontonan = 'banyak'
    else :
        tontonan = 'sedikit'

    context = {
    'watchlist': data_watchlist,
    'nama': 'Muhammad Ruzain',
    'npm' : '2106750250',
    'tontonan' : tontonan
    }
    return render(request, "watchlist.html", context)

def show_watchlist_xml(request):
    data_watchlist = Watchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_watchlist_json(request):
    data_watchlist = Watchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")