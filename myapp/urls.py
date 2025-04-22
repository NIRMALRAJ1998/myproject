from django.urls import path
from . import views

urlpatterns = [
    path('simple/', views.simple_view, name='simple_view'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.success_page, name='success_page'),
    path('about/', views.about, name='about'),
    path('properties/',views.properties,name='properties'),
    path('services/',views.services, name='services')


]