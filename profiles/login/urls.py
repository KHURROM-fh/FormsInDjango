from django.urls import path, include
from login import views
# from . import django_form
urlpatterns = [
    path('', views.loginHome, name='home'),
    path('form/', views.loginform, name='form'),
    path('djangoForm/', views.djangoForm, name='djform'),
]