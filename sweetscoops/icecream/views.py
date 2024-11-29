from django.shortcuts import render
from .models import Icecream,Category,Tag
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

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

# @method_decorator(staff_member_required,name="dispatch")
class IcecreamCreateView(CreateView):
    model=Icecream
    fields="__all__"
    success_url="/icecream/menu"
    template_name = "icecreams/icecream_form.html"

# @method_decorator(staff_member_required,name="dispatch")
class IcecreamUpdateView(UpdateView):
    model= Icecream
    fields="__all__"
    success_url="/icecream/menu"
    template_name = "icecreams/icecream_form.html"
    
# @method_decorator(staff_member_required,name="dispatch")
class IcecreamDeleteView(DeleteView):
    model=Icecream
    success_url="/icecream/menu"
    template_name = "icecreams/icecream_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["relatedIcecreams"]=Icecream.objects.all()
        return context

def Categories(request):
    return render(request,"categories/categories_list.html",{"categories":Category.objects.all()})

def TopIceCream(request):
    top_icecreams=Tag.objects.get(id=7).icecreams.all()
    return render(request,"top_icecreams/top_icecreams.html",{"top_icecreams":top_icecreams})