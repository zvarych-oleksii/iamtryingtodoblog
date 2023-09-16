import os
from pathlib import Path
from django.core.files.images import ImageFile
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from django.views.generic import DetailView
from ..models import posts, categories
from ..forms import *
from django.shortcuts import render


class BlogCreationView(FormView):
    template_name = "creation_pages/post_creation.html"
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

'''
def file_form(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            model_info = docx_file_parse(request.FILES['file'])
            obj = Post_written()
            obj.title = model_info.get("Title")
            obj.author = request.user.profile
            obj.image = ImageFile(open(model_info.get("Image"), "rb"))
            obj.save()
            for i in model_info.get("Categories").split(','):
                obj.category.add(Category.all_categories.get(name=i))
            obj.save()
            os.remove(model_info.get("Image"))
            FileForm()
    return render(request, "creation_pages/file_create.html", {"form": FileForm})

'''


