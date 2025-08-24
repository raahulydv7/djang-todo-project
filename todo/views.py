from django.shortcuts import render,redirect
from .models import Category,Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

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

