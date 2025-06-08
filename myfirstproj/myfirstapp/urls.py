from django.urls import path
from . import views

urlpatterns = [
    path('class', views.MyView.as_view()),
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('reservation/', views.reservation, name='reservation'),
    path('book/', views.book, name='book'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
]   