from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home,name='home'),
    path('contact',views.Contact,name='contact'),
    path('about',views.About,name='about'),
    path('doctors',views.Docters,name='doctors'),
    path('depart',views.Department,name='department'),
]