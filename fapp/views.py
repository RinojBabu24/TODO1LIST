from django.shortcuts import render, redirect
from .forms import  todoForm
from .models import Todo
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage




def demo(request):
    todo=Todo.objects.all()
    return render(request,'index.html',{'todo':todo})


def insert(request):
    if request.method == 'POST':
        Task = request.POST['Task']
        Date = request.POST['Date']
        Time = request.POST['Time']
        

        todos=Todo(
            Task=Task,  
            Date=Date,
            Time=Time,
            
        )
        todos.save()
       
        return redirect('fapp:demo')
    return render(request, 'home.html')


def edit(request,todo_id):
     todo = Todo.objects.all()
     sel_todo =Todo.objects.get(id=todo_id)
     context={'todo': todo,'sel_todo': sel_todo,'todo_id':todo_id}
     return render(request,'home.html',context)


def update(request,todo_id):
    if request.method=='POST':
        todo = Todo.objects.get(id=todo_id)
        todo.Task = request.POST['Task']
        todo.Date = request.POST['Date']
        todo.Time = request.POST['Time']
        todo.save()
    
        return redirect('fapp:demo')
    return render(request, 'home.html')


def insert_task(request):
     todo= Todo.objects.all()
     context={'todo':todo}
     return render(request,'home.html',context)

def delete(request,id):
        # if request.method=='POST':
            todo=Todo.objects.get(id=id)
            todo.delete()
            return redirect('fapp:demo')
        # return render(request,'delete.html')




