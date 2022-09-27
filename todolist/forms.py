from cProfile import label
from django import forms

class CreateTask(forms.Form) :
    judul = forms.CharField(label='Judul', max_length=100)
    deskripsi = forms.CharField(label = 'Deskripsi',widget=forms.Textarea)
    