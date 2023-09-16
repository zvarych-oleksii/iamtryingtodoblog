from django.contrib import admin
from .models import posts
from .models import categories
from .models import reviews
from .models import raiting

admin.site.register(posts.Post_written)
admin.site.register(categories.Category)
admin.site.register(reviews.Reviews)
admin.site.register(raiting.Rating)
admin.site.register(raiting.RatingStar)
admin.site.register(categories.SubCategory)
