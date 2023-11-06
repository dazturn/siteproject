from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexAPIView, name='home'),
    path('aptitude/', views.ProfAPIView, name='aptitude'),
    path('projects/', views.ProjectAPIView, name='projects'),
]