from cProfile import label
from django import forms

class CreateTask(forms.Form) :
    judul = forms.CharField(max_length=100)
    deskripsi = forms.CharField(max_length=100)
    