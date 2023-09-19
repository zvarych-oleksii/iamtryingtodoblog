from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import PostView, BlogCreateView, home_page

urlpatterns = [
    path('post_single/<slug:slug>', PostView.PostDetailView.as_view(), name='PostDetailView'),
    path('post_list/', PostView.PostListView.as_view(), name='PostListView'),
    path("", home_page.Index, name="Index"),
#   path("game_single/<slug:slug>", GameDetailView.GameDetailsView, name="game_single"),
#    path("game_list_view/", GameListView.GameListView.as_view(), name="GameListUrl"),
    path("post_create/", login_required(PostView.BlogCreationView.as_view()), name="BlogCreationView"),
#    path("testing/", file_form , name="FileCreation"),
]
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
