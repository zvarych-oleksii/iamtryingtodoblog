from django.views.generic import DetailView
from ..models import Post_written

class PostDetailView(DetailView):
    model = Post_written
    slug_url_kwarg = "slug"
    template_name = "detail/post_detail_view.html"
    context_object_name = "detail_post"
    def get_object(self):
        obj = super().get_object()
        obj.views = obj.views + 1
        obj.save
        return obj
