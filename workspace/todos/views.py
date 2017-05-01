from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Todo
import time
def index(request):
    todos= Todo.objects.all()[:10]
    context={
        'todos':todos
    }
    return render(request, 'index.html', context)
    
def details(request, id):
    todo=Todo.objects.get(id=id)
    context={
        'todo':todo
    }
    #todo.delete()
    return render(request, 'details.html', context)
    
def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'add.html')

def delete(request, id):
    todo=Todo.objects.get(id=id)
    context={
        'todo':todo
    }
    todo.delete()
    return redirect('/todos')
    
def timer(request):
    return HttpResponse(time.strftime("%c"))