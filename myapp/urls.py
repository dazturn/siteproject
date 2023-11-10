from django.urls import path
from . import views
# 
urlpatterns = [
    path('', views.IndexAPIView.as_view(), name='home'),
    path('aptitude/', views.ProfAPIView.as_view(), name='aptitude'),
    path('projects/', views.ProjectAPIView.as_view(), name='projects'),
]