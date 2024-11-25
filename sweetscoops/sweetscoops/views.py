from django.shortcuts import render


def home(request):
    return render(request,"index.html",{})

def dishes(request):
    return render(request,"dishes.html")

def about(request):
    return render(request,"about.html")