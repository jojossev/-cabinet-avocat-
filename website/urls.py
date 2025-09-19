from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('equipe/', views.equipe, name='equipe'),
    path('equipe/<int:avocat_id>/', views.avocat_detail, name='avocat_detail'),
    path('contact/', views.contact, name='contact'),
]
