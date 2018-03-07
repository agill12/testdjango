from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm,EditTodoItemForm

# Create your views here.



def get_todo_page(request): 
    
    if request.method=="POST":
        form=TodoItemForm(request.POST)
        print("Its the POST")   
        if form.is_valid():
            form.save()
        
    else:
        print("Its a GET")
    form=TodoItemForm()
    items=TodoItem.objects.all()
    return render(request, 'todo/todo.html',{'items':items,'form':form})
    
    
def delete_todo_item(request,id):
    item= get_object_or_404(TodoItem,pk=id)
    item.delete()
    return redirect('http://todolist-agill1.c9users.io:8080/')


def toggle_todo_item(request,id):
    item= get_object_or_404(TodoItem,pk=id)
    
    item.done = not item.done
         
    item.save()

    
    return redirect('http://todolist-agill1.c9users.io:8080/')
    
    
def edit_todo_item(request,id):
    item= get_object_or_404(TodoItem,pk=id)
    if request.method== 'POST':
        
        form=EditTodoItemForm(request.POST,instance=item)
        print("Its the POST") 
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        print("Its the GET")
    
    form=EditTodoItemForm(instance=item)
    return render(request, 'todo/todoitemform.html',{'form':form})
    