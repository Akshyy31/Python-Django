from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home,name='home'),
    path('contact',views.Contact),
    path('about',views.About),
    path('doctors',views.Docters),
    path('depart',views.Department),
]