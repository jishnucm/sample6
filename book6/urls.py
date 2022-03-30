from django.urls import path
from .import views

urlpatterns = [
    path('admin2/', views.index),
    path('login/',views.login, name="login")
]
