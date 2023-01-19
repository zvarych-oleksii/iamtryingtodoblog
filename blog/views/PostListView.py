from django.views.generic import ListView
from ..models import Post_written, Game, Category


class PostListView(ListView):
    model = Post_written
    template_name = "lists/post_list_view.html"
    context_object_name = "list_of_posts"
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({
            "category":Category.all_categories.all()
        })
        return context
    def get_queryset(self):
        return Post_written.all_posts.order_by("-date")