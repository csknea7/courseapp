from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('anasayfa/', views.index, name='anasayfa'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]