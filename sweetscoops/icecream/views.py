from django.shortcuts import render
from .models import Icecream
from django.views.generic import ListView,DetailView

# Create your views here.
def dishes(request):
    return render(request,"dishes.html",{})

class IcecreamList(ListView):
    model = Icecream 
    template_name="icecreams/icecream_list.html"

class IcecreamDetail(DetailView):
    model = Icecream 
    template_name="icecreams/icecream_detail.html"