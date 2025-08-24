from django.shortcuts import render,redirect, get_object_or_404
from .models import Category,Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

@login_required
def todos(request):
    if request.user.role == 'Admin':
        todos = Todo.objects.all()
    else:
        todos = Todo.objects.filter(user=request.user)
    
    return render(request, 'todo/todos.html', {'todos': todos})

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False) 
            todo.user = request.user       
            todo.save()
            return redirect('todos')
    else:
        form = TodoForm()
    return render(request, 'todo/create_todo.html', {'form': form})


@login_required
def update_todo(request,slug):
    todo = get_object_or_404(Todo,slug=slug)
    
    if todo.user != request.user and not request.user.is_superuser:
        return redirect('todos')
    
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos')
        
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/update_todo.html', {'form': form})


@login_required
@require_POST
def delete_todo(request,slug):
    todo = get_object_or_404(Todo,slug=slug)
    todo.delete()
    return redirect('todos')