from django.shortcuts import render, redirect
from .models import AddList

# Create your views here.
def index(request):
    todo = AddList.objects.all()
    if request.method == 'POST':
        new_title = AddList(
            title = request.POST['title']
        )
        new_title.save()
        return redirect('/')

    return render(request, 'index.html', {'todo':todo})

def delete(request, pk):
    todo_delete = AddList.objects.get(id=pk)
    todo_delete.delete()
    return redirect('/')


