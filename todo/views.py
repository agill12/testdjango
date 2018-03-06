from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm
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
    return HttpResponse("You deleted"+ " "+ item.name)
