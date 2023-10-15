from rest_framework import generics, permissions
from .models import Blog
from .serializers import BlogSerializerGET, BlogSerializerPOST, BlogSerializerPUT, BlogSerializerDelete

class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerPOST
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AuthorBlogsView(generics.ListAPIView):
    serializer_class = BlogSerializerGET
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtrar los blogs por el autor actualmente autenticado
        return Blog.objects.filter(author=self.request.user)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerGET
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        if instance.author == self.request.user:
            instance.delete()
        else:
            pass
        # Aquí puedes personalizar el manejo de errores si el usuario no es el autor del blog