from django.views.generic import (
    CreateView,
    DetailView
    UpdateView
    DeleteView
    ListView
)
from .models import Post
from django.urls import reverse_lazy


class PostListView(ListView):
    template_name = "post/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "post/detait.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "post/new.html"
    model = Postfields = ["title", "subtitle", "author", "body", "active"]    

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    field = ["title", "subtitle","body","active"]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Posts
    success_url = reverse_lazy("list")        
# Create your views here.
