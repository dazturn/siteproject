from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexAPIView.as_view(), name='home'),
    path('aptitude/', views.ProfAPIView.as_view(), name='aptitude'),
    path('projects/', views.ProjectAPIView.as_view(), name='projects'),
]

# Static files to serve
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)