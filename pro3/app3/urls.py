from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
path('about/',views.about,name='about'),
path('department/',views.Departments,name='department'),
path('contact/',views.contact,name='contact'),
path('booking/',views.booking, name='booking'),
path('doctors/',views.doctors,name='doctors'),

]