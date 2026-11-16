
from django.shortcuts import render, redirect
from .models import Student

def index(request):
    data=Student.objects.all()
    return render(request, 'app/index.html', {'data': data})
def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect('/')
    return render(request, 'app/index.html')
def updateData(request,id):
    d=Student.objects.get(id=id)
    return render(request,'app/edit.html',{'d':d})
def updateData(request,id):
    d=Student.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        X=Student.objects.get(id=id)
        X.name=name
        X.email=email
        X.age=age
        X.gender=gender
        X.save()
        return redirect('/')
    return render(request,'app/edit.html',{'d':d})
def deletData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect('/')
