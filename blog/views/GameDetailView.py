from django.views.generic import DetailView
from ..models import *
from django.shortcuts import render


class GameDetail(DetailView):
    model = Game
    slug_url_kwarg = "slug"
    template_name = "detail/game-single.html"
    context_object_name = "game"


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def GameDetailsView(request, slug):
    game_details = Game.all_list.get(slug=slug)
    ip = get_client_ip(request)
    if GameViews.objects.filter(IPAddres=ip).exists():
        game_details.views.add(GameViews.objects.get(IPAddres=ip))
    else:
        GameViews.objects.create(IPAddres=ip)
        game_details.views.add(GameViews.objects.get(IPAddres=ip))
    return render(request, "detail/game-single.html", context={"game": game_details})


