import imp
from django.shortcuts import render
from mywatchlist.models import Watchlist

# Create your views here.
def show_watchlist(request):
    data_watchlist = Watchlist.objects.all()
    context = {
    'watchlist': data_watchlist,
    'nama': 'Muhammad Ruzain',
    'npm' : '2106750250'
    }
    return render(request, "watchlist.html", context)
