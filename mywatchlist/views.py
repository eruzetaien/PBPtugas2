import imp
from django.shortcuts import render
from mywatchlist.models import Watchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist = Watchlist.objects.all()
    context = {
    'watchlist': data_watchlist,
    'nama': 'Muhammad Ruzain',
    'npm' : '2106750250'
    }
    return render(request, "watchlist.html", context)

def show_watchlist_xml(request):
    data_watchlist = Watchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_watchlist_json(request):
    data_watchlist = Watchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")