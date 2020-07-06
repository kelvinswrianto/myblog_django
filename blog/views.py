from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
# Create your views here.

class PostListView(LoginRequiredMixin, ListView):
    paginate_by = 6
    template_name = 'blog/blog_index.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'blog/blog_detail.html'
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = self.get_object()
        extra_context = {
            'update_permission' : True if self.request.user == post.author else False
        }
        context.update(extra_context)
        return context
    

    
# @login_required
class PostCreateview(LoginRequiredMixin, CreateView):
    template_name = 'blog/blog_create.html'
    model   = Post
    fields  = (
        'title',
        'content',
    )
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    template_name = 'blog/blog_update.html'
    model   = Post
    fields  = (
        'title',
        'content',
    )
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'blog/blog_delete.html'
    model = Post
    success_url = '/blog/'
    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        return False

class SearchListView(LoginRequiredMixin, ListView):
    paginate_by = 6
    template_name = 'blog/blog_search.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        if object_list == None:
            self.template_name = 'blog_search_404.html'

        return object_list