from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def home(request):
    return render(request, "home.html", {"title" : "My Home"})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def add_student(request):
    if request.method == "POST":
        stu_name = request.POST.get("stu_name").strip()
        stu_email = request.POST.get("stu_email").strip()
        if not stu_name and not stu_email:
            return render(request, "add-student.html", {"err_msg" : "Plase fill the form"})
        isExists = Student.objects.filter(email=stu_email)
        if isExists:
            return render(request, "add-student.html", {"err_msg" : "Email already exists"})
        Student.objects.create(name=stu_name, email=stu_email)
        return redirect("home")
    return render(request, "add-student.html")
