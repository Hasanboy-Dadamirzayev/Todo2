from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.views import View
from .models import *
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            tasks = Tasks.objects.filter(owner=request.user).order_by('-status', '-date')
            context = {
                'status': Tasks.CHOICES,
                'tasks': tasks,
            }
            return render(request, 'index.html', context=context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Tasks.objects.create(
                title = request.POST.get('title'),
                details = request.POST.get('details'),
                date = request.POST.get('date') if request.POST.get('date') else None,
                status = request.POST.get('status'),
                owner = request.user,
            )
            return self.get(request)

def confirm_view(request, task_id):
    task = Tasks.objects.get(id=task_id)
    context = {
        'task': task
    }
    return render(request, 'delete_confirm.html', context)

def delete_view(request, task_id):
    if request.user.is_authenticated:
        task = Tasks.objects.get(id=task_id, owner=request.user)
        task.delete()
        return redirect('home')
    return redirect('login')


class UpdateView(View):
    def get(self, request, task_id):
        if request.user.is_authenticated:
            task = get_object_or_404(Tasks, id=task_id, owner=request.user)
            return render(request, 'edit_confirm.html', {
                'task': task,
                'status': Tasks.CHOICES,
            })
        return redirect('login')



    def post(self, request, task_id):
        if request.user.is_authenticated:
            task = get_object_or_404(Tasks, id=task_id, owner=request.user)  # Debug

            task.title = request.POST.get('title')
            task.details = request.POST.get('details')
            task.status = request.POST.get('status')
            task.save()

            return redirect('home')
        return redirect('login')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


    def post(self, request):
        if request.POST.get('password1') != request.POST.get('password2') or request.POST.get('username') in User.objects.values_list('username', flat=True):
            return redirect('register')
        User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password1'),
        )
        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password1')
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('login')




