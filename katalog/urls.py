from django.urls import path
from katalog.views import show_katalog
from katalog.views import show_xml


# TODO: Implement Routings Here

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
    path('xml/', show_xml, name='show_xml'),
]