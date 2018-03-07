from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm, EditTodoItemForm

# Create your views here.
def get_index(request):
    if request.method == "POST":
        print("It's the POST")        
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        print("It's the GET")        

    form = TodoItemForm()
    items = TodoItem.objects.all()
    return render(request, "todo/index.html", {'items': items, 'form': form})


def edit_todo_item(request, id): 
    item = get_object_or_404(TodoItem, pk=id)

    if request.method == "POST":
        print("It's the POST")
        form = EditTodoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("todo_index")
    else:
        print("It's the GET")
        
    form = EditTodoItemForm(instance=item)
    return render(request, "todo/todo_item_form.html", {'form': form})



def delete_todo_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    item.delete()
    return redirect("todo_index")
    
def toggle_status(request, id):
    print(request.method)
    item = get_object_or_404(TodoItem, pk=id)
    item.done = not item.done
    item.save()
    return redirect("todo_index")