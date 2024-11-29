from django.urls import path
from . import views

urlpatterns = [
    path('',views.dishes,name="dishes"),
    path('menu/',views.IcecreamList.as_view(),name ="icecream-list"),
    path('menu/<int:pk>',views.IcecreamDetail.as_view(),name = "icecream-detail"),
    path('search',views.search,name="search"),
    path('create-icecream/',views.IcecreamCreateView.as_view(),name="create-product"),
    path('update-icecream/<int:pk>/',views.IcecreamUpdateView.as_view(),name="product-update"),
    path('delete-icecream/<int:pk>/',views.IcecreamDeleteView.as_view(),name="delete-product"),
    path('categories/',views.Categories,name="categories"),
    path('top-icecreams/',views.TopIceCream,name="top-icecreams"),
    path('<slug:slug>/',views.CatergoryDetailView.as_view(),name="category-detail"),
]


