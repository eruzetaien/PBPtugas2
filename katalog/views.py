from django.shortcuts import render
from katalog.models import CatalogItem
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_katalog': data_barang_katalog,
    'nama': 'Muhammad Ruzain',
    'npm' : '2106750250'
    }
    return render(request, "katalog.html", context)

def show_xml(request):
    data =CatalogItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
