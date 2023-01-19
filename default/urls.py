from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from default.views import Index

urlpatterns = [
    path("", Index.as_view(), name="Index")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
