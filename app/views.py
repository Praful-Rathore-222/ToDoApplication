from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    app = App.objects.all()

    form = AppForm()

    if request.method == "POST":
        form = AppForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect ('/')   


    context = {'apps': app, 'form': form}
    return render(request,'app/list.html', context)

def update(request, id):

    app= App.objects.get(id=id)
    form = AppUpdateForm(instance=app)
  

    if request.method == "POST":
       form = AppUpdateForm(request.POST, instance=app)
       print(1111111111111111111111111111111111111111111)

       if form.is_valid:
            print(222222222222222222222222222222222222222)
            form.save()
            return redirect ('/')

    context= {'form' : form}
    return render(request,'app/update.html', context)

def delete(request, id):
   item = App.objects.get(id=id)
   
   if request.method == "POST":
       item_ID = request.POST.get('item_id')
       App.objects.get(id=item_ID).delete()
       return redirect('/')

   context = {'item': item}
   return render(request,'app/delete.html',context)

