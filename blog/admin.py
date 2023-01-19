from django.contrib import admin

from .models import Post_written
from .models import Category, SubCategory
from .models import Reviews
from .models import Rating
from .models import RatingStar
from .models import Game, GameViews

admin.site.register(Post_written)
admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(SubCategory)
admin.site.register(Game)
admin.site.register(GameViews)