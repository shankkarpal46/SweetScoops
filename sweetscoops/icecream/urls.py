from django.urls import path
from . import views

urlpatterns = [
    path('',views.dishes,name="dishes"),
    path('menu/',views.IcecreamList.as_view(),name = "icecream-list"),
    path('menu/<int:pk>',views.IcecreamDetail.as_view(),name = "icecream-detail"),
]

