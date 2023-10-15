from django.urls import path
from .views import BlogListView, BlogDetailView, AuthorBlogsView

urlpatterns = [
    # Lista de blogs y creación de un nuevo blog
    path('blogs/', BlogListView.as_view(), name='blog-list'),

    # Detalles, actualización y eliminación de un blog
    path('<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),

    # Lista de blogs de un autor específico
    path('author/', AuthorBlogsView.as_view(), name='author-blogs'),
]
