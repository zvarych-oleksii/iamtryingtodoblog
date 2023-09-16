'''from django.views.generic import ListView
from ..models import *


class GameListView(ListView):
    model = Game
    template_name = "lists/GameListView.html"
    context_object_name = "games"

    def get_context_data(self, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)
        context.update({
            "subcategory":SubCategory.all_subcategories.all()
        })
        return context
    
    def get_queryset(self):
        return Game.all_list.order_by("title_of_game")

'''
