from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='upload-home'),
    path('about/', views.about, name='upload-about'),
]