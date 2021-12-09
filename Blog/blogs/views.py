from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .form_styles import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

#ListView = it list out all the records of a chosen model in database, and it usally called by a for loop
#DetailView = it bring out the details of one record of a chosen model in database instead of listing all like ListView
#CreateView = it create a new intance of an existing model in the database, and it's important to specify the field it should create, 
#if we are not using form class. it's through CreateView we handle form
class HomeListView(ListView):
    model = Post
    template_name = "home.html"
    ordering = '-date_uploaded'


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article.html"

class AddPostCreateView(CreateView):
    model = Post
    template_name = "add_post.html"
    form_class = PostForm
    #specifying the field to create
    #fields = ['title','body']

class EditPostUpdateView(UpdateView):
    model = Post
    template_name = "edit_post.html"
    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('blog:home')

def CategoryView(request, cate):
    category = Post.objects.all().filter(category=cate)
    return render(request, 'category.html', {'cate':cate, 'posts_category': category})