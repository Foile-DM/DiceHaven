from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('reservation', views.reservation, name='reservation'),
    path('reservation_submit', views.reservation_submit, name='reservation_submit'),
    path('contact', views.contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
