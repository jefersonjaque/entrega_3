from django.urls import path
from .views import home,cajas

urlpatterns = [
    path('',home,name="home"),
    path('cajas/',cajas,name="cajas")
]
