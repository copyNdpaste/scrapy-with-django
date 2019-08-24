from django.conf import settings
from django.conf.urls import static
from django.urls import re_path, path
from django.views.generic import TemplateView

from main import views

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='main/index.html'), name='home'),
    re_path(r'^api/crawl/', views.crawl, name='crawl'),
    path('api/showdata/', views.show_data, name='show_data')
]

if settings.DEBUG:
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
