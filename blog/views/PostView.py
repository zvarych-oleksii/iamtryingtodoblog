from django.views.generic import DetailView
from django.views.generic import ListView, FormView
from ..models import posts, categories
from ..forms import *


class PostDetailView(DetailView):
    model = posts.Post_written
    slug_url_kwarg = "slug"
    template_name = "posts/detail_view.html"
    context_object_name = "detail_post"
    def get_object(self):
        obj = super().get_object()
        obj.views = obj.views + 1
        obj.save
        return obj


class PostListView(ListView):
    model = posts.Post_written
    template_name = "posts/list_view.html"
    context_object_name = "list_of_posts"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({
            "category":categories.Category.all_categories.all()
        })
        return context

    def get_queryset(self):
        return posts.Post_written.all_posts.order_by("-date")


class BlogCreationView(FormView):
    template_name = "posts/creation.html"
    form_class = BlogCreationForm

    def get_context_data(self, **kwargs):
        context = super(BlogCreationView, self).get_context_data(**kwargs)
        context.update({
            'form': BlogCreationForm()
        })
        return context
    
    def form_valid(self, form):
        triger = form.save(commit=False)
        triger.author = self.request.user.profile
        triger.save()
        return redirect("Index")
