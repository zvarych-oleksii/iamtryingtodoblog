from django.shortcuts import render
from django.views.generic import ListView

from ..models import *
'''class Index(ListView):
    model = Game
    template_name = 'index/index.html'
    context_object_name = 'games'''
def Index(request):
    context = {
        "subcategory":SubCategory.all_subcategories.all(),
        "category":Category.all_categories.all(),
        "games":Game.all_list.all().order_by("-created")[0:3],
        "posts":Post_written.all_posts.all().order_by("views")[0:4],
        "head_posts":Post_written.all_posts.all().order_by("title")[0:3],
    }
    return render(request, "index/index.html", context)