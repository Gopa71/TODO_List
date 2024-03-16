from django.shortcuts import render,redirect
from .models import Task
# from .form import Form
# Create your views here.
def home(req):
    data=Task.objects.all
    if req.method=='POST':
        task=req.POST.get('task')
        priority=req.POST.get('priority')
        date=req.POST.get('date')
        tk=Task(task=task,priority=priority,date=date)
        tk.save()
       
    return render(req,'index.html',{'data':data})
def delete(req,id):
    if req.method=='POST':
        data=Task.objects.get(id=id)
        data.delete()
        return redirect('/')
    return render(req,'delete.html')

# def update(req,id):
#         todo=Task.objects.get(id=id)
#         form=Form(req.POST or None, instance=todo)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
        
#         return render(req,'add.html',{'form':form,'todo':todo})

def update(req,id):
    data=Task.objects.get(id=id)
    if req.method=='POST':
        task=req.POST.get('task')
        priority=req.POST.get('priority')
        date=req.POST.get('date')
        Task.objects.filter(id=id).update(task=task,priority=priority,date=date)
        return redirect('/')
    return render(req,'add.html',{'data':data})