from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class HomeListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-date')[:3]

    def get_context_data(self, **kwargs):
        ctx = super(HomeListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница'
        return ctx

class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(BlogListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Страница блога'
        return ctx

class BlogDeatailView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super(BlogDeatailView, self).get_context_data(**kwargs)
        ctx['title'] = f'Запись - {Post.title}'
        return ctx