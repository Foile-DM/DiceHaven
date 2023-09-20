from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('reservation', views.reservation, name='reservation'),
    path('reservation_submit', views.reservation_submit, name='reservation_submit'),
    path('contact', views.contact, name='contact'),
]
