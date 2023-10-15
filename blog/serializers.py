from .models import Blog

from rest_framework.serializers import ModelSerializer


class BlogSerializerGET(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['title', 'description', 'content', 'pub_data', 'author']


class BlogSerializerPOST(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['title', 'description', 'content']


class BlogSerializerPUT(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['title','description','content']

class BlogSerializerDelete(ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'