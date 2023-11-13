from django.urls import path
from .views import IndexAPIView, ProfAPIView, ProjectAPIView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexAPIView.as_view(), name='home'),
    path('aptitude/', ProfAPIView.as_view(), name='aptitude'),
    path('projects/', ProjectAPIView.as_view(), name='projects'),
]

# Static files to serve
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)