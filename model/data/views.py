from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Note

def login(request):
    if request.method =="POST":
        uname = request.POST["uname"]
        upass = request.POST["upass"]

        User = auth.authenticate(username = uname , password = upass)
        

        if User is not None :
            auth.login(request,User)
            return redirect("dashboard")
        
        else :
            return redirect("login")

        
    return render(request,'login.html')

def dashboard(request):
    User = request.user
    if request.method =='POST':
        # User = request.user
        
        title = request.POST["utitle"]
        desc = request.POST["utextarea"]

        new_note = Note.objects.create(title = title ,
                                        description = desc,
                                        user = User)
        new_note.save()

        return redirect("notes")
    data = {
        "User":User
    }
    return render(request,'dashboard.html' ,data)

def notes(request):
     user = request.user
     notes = Note.objects.filter(user = user)
     
     data={
         "user": user,
         "notes":notes
                 }
     return render(request,"notes.html",data)
     

   

def signup(request):

    if request.method == "POST":
        uname= request.POST["uname"]
        fname= request.POST["fname"]
        lname= request.POST["lname"]
        upass= request.POST["upass"]

        new_user = User.objects.create(
            username = uname,
            first_name=fname,
            last_name= lname,
        )
        new_user.set_password(upass)
        new_user.save() 
        return redirect("login")

    return render(request,'signup.html')


def logout(request):
    auth.logout(request)
    return redirect("login")

def edit(request ,slug):
    note = Note.objects.get(slug=slug)
    if request.method=="POST":
        new_title = request.POST["utitle"]
        new_desc = request.POST["udesc"]
        note.title = new_title
        note.description = new_desc
        note.save()

        return redirect("notes")
    
    parameter={
        "note":note
    }

    return render(request,"edit.html",parameter)

def delete(request,id):
    note =Note.objects.get(id=id)
    note.delete()
    return redirect("notes")
