from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    context={"name":"uday","course":"btech"}
    return render(request,"home.html",context)
def about(request):
    return render(request,"about.html")
def projects(request):
    return render(request,"projects.html")
def contact(request):
    if(request.method=="POST"):
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        concern=request.POST["concern"] 
        ins=Contact(name=name,email=email,phone=phone,concern=concern)
        ins.save()
        print("values are inserted")
    return render(request,"contact.html")
def project1(request):
    return render(request,"project1.html")
def project2(request):
    return render(request,"project2.html")
def project3(request):
    return render(request,"project3.html")
def project4(request):
    return render(request,"project4.html")


