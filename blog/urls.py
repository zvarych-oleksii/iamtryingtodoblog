from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from .views import PostDetailView, PostListView, GameDetailView, GameListView, BlogCreateView, home_page

urlpatterns = [
    path('post_single/<slug:slug>', PostDetailView.PostDetailView.as_view(), name='PostDetailView'),
    path('post_list/', PostListView.PostListView.as_view(), name='PostListView'),
    path("", home_page.Index, name="Index"),
    path("game_single/<slug:slug>", GameDetailView.GameDetailsView, name="game_single"),
    path("game_list_view/", GameListView.GameListView.as_view(), name="GameListUrl"),
    path("test_creation_form/", BlogCreateView.BlogCreationView.as_view(), name="BlogCreationView"),
#    path("testing/", file_form , name="FileCreation"),
]
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
