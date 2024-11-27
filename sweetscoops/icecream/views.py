from django.shortcuts import render
from .models import Icecream,Category
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


def search(request):
    keyword=request.GET.get("keyword")
    icecreams= Icecream.objects.all().filter(icecream_name__icontains = keyword)
    return render(request,"dishes.html",{"object_list":icecreams})
    

class CatergoryDetailView(DetailView):
    model = Category
    template_name = "categories/category_detail.html"
    slug_field = "category_slug"
    context_object_name = "category_obj"



