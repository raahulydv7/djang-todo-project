from django.shortcuts import render,redirect, get_object_or_404
from .models import Category,Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

@login_required
def todos(request):
    status = request.GET.get('status')
    category_id = request.GET.get('category')
    search_query = request.GET.get('search', '')

    if request.user.role == 'Admin':
        todos = Todo.objects.all()
    else:
        todos = Todo.objects.filter(user=request.user)
    
    if status:
        todos = todos.filter(status=status)
    
    if category_id:
        todos = todos.filter(category_id=category_id)
    
    if search_query:
        todos = todos.filter(title__icontains=search_query)
    

    categories = Category.objects.all()

    return render(request, 'todo/todos.html', {
        'todos': todos,
        'categories': categories,
        'selected_status': status,
        'selected_category': category_id,
    })

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