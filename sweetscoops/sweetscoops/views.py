from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from  .form import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from icecream.models import Category,Tag

def home(request):
    top_icecreams=Tag.objects.get(id=7).icecreams.all()
    return render(request,"index.html",{"categories":Category.objects.all(),"top_icecreams":top_icecreams})

def dishes(request):
    return render(request,"dishes.html")

def about(request):
    return render(request,"about.html")

def user_login(request):
    if request.method=="GET":
       return render(request,"login.html")
    
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print(request.user.first_name)
            return HttpResponseRedirect("/")
        else:
            return render(request,"login.html",{"message":"Log in failed"})
        
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")

def register(request):
    if request.method=="GET":
        # form=UserCreationForm()
        form=CustomUserCreationForm()
        return render(request,"register.html",{"form":form})
    else:
        # form=UserCreationForm(request.POST)
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login")
        return render(request,"register.html",{"form":form})
    
def carausel(request):
    icecream_of_year = Tag.objects.get(id=5).icecreams.all()
    return render(request,"carausel/swiper.html",{"icecream_of_year":icecream_of_year})