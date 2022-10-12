from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from todolist.forms import CreateTask
from todolist.models import Task

import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.core import serializers
from django.urls import reverse


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    data_todolist = Task.objects.all()
    context = {
    'todolist': data_todolist,
    'nama': 'Muhammad Ruzain',
    'npm' : '2106750250',
    'user': user
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')


# without ajax
def create_task(request):
    form = CreateTask()

    if request.method == "POST":
        form = CreateTask(request.POST)
        if form.is_valid():
            judul = request.POST.get("judul")
            deskripsi = request.POST.get("deskripsi")
            user = request.user
            new_data = Task(user=user, title=judul, description=deskripsi)
            new_data.save()
            return redirect('todolist:show_todolist')

    context = {'form':form}
    return render(request, 'create_task.html', context)

# def change_status(request, id):
#     task = Task.objects.get(id=id)
#     task.is_finished = not task.is_finished
#     task.save()
#     return redirect('todolist:show_todolist')

# def delete(request, id):
#     task = Task.objects.get(id=id)
#     task.delete()
#     return redirect('todolist:show_todolist')

def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_task(request):
    if request.method == 'POST':
        judul     = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        user = request.user

        Task.objects.create(
            user      = user,
            title     = judul,
            description = deskripsi,
        )
    return JsonResponse({}, status=200)

def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        
    return JsonResponse({}, status=200)


def change_status(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.is_finished = not task.is_finished
        task.save()
        
    return JsonResponse({}, status=200)
