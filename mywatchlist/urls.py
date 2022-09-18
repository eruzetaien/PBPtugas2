from django.urls import path
from mywatchlist.views import show_watchlist

# TODO: Implement Routings Here

app_name = ''

urlpatterns = [
    path('html/', show_watchlist, name='show_watchlist'),
]