from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from django.http import HttpResponse

class HomeView(View):
    def get(self, request):
        tasks = Tasks.objects.order_by('-status', '-date')
        context = {
            'status': Tasks.CHOICES,
            'tasks': tasks,
        }
        return render(request, 'index.html', context=context)

    def post(self, request):
        Tasks.objects.create(
            title = request.POST.get('title'),
            details = request.POST.get('details'),
            date = request.POST.get('date') if request.POST.get('date') else None,
            status = request.POST.get('status'),
        )
        return self.get(request)

def confirm_view(request, task_id):
    task = Tasks.objects.get(id=task_id)
    context = {
        'task': task
    }
    return render(request, 'delete_confirm.html', context)

def delete_view(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('home')


class UpdateView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Tasks, id=task_id)
        return render(request, 'edit_confirm.html', {
            'task': task,
            'status': Tasks.CHOICES,
        })

    def post(self, request, task_id):
        task = get_object_or_404(Tasks, id=task_id)  # Debug

        task.title = request.POST.get('title')
        task.details = request.POST.get('details')
        task.status = request.POST.get('status')
        task.save()

        return redirect('home')



