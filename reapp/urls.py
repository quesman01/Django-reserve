# urls.py
from django.urls import path
from . import views
from .views import reservation_list

urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('success/', views.success, name='success'),
     path('reservations/', reservation_list, name='reservation_list'),
]
