from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import *


def list(request):
    return render(request,"list.html")

def Todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        details = request.POST.get("details")
        startdate = request.POST.get("startdate")
        enddate = request.POST.get("enddate")
        todocreate = tododetails.objects.create(title=title,details=details,startdate=startdate,enddate=enddate)
        print(todocreate)
        return redirect('todo')
    details = tododetails.objects.all()
    return render(request,"todo.html",{"details":details})

def delete(request,id):
    query = tododetails.objects.get(pk=id)
    query.delete()
    return redirect('todo')

def Todoedit(request,id):
     data=tododetails.objects.get(pk=id)

     if request.method == "POST":
        data.title = request.POST['title']
        data.details = request.POST['details']
        data.startdate = request.POST['startdate']
        data.enddate = request.POST['enddate']
        data.save()

        return redirect('todo')
     return render(request,"edit.html",{'edit':data})