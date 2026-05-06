from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('templates/web/', views.web_templates_view, name='web_templates'),
    path('templates/mobile/', views.mobile_templates_view, name='mobile_templates'),
]
