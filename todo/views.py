
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

