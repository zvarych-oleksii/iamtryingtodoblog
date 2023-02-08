from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('post_single/<slug:slug>', PostDetailView.as_view(), name='PostDetailView'),
    path('post_list/', PostListView.as_view(), name='PostListView'),
    path("", Index, name="Index"),
    path("game_single/<slug:slug>", GameDetailsView, name="game_single"),
    path("game_list_view/", GameListView.as_view(), name="GameListUrl"),
    path("test_creation_form/", BlogCreationView.as_view(), name="BlogCreationView"),
    path("testing/", file_form , name="FileCreation"),
]
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)