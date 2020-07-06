from django.urls import path
from .views import PostCreateview, PostListView, PostDetailView, PostUpdateView, PostDeleteView, SearchListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', PostListView.as_view(), name='blog-index'),
    path('<int:pk>/detail/', PostDetailView.as_view(), name='blog-detail'),
    path('create/', login_required(PostCreateview.as_view()), name='blog-create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
    path('search/', SearchListView.as_view(), name='blog-search'),
]