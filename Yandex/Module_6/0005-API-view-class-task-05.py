"""
Задача
------
Напишите view-класс APIPost(), унаследовав его от APIView.
Он будет работать с queryset, содержащим все объекты модели Post. 

При POST-запросе этот класс должен создавать новый объект модели Post и возвращать его, 
а по GET-запросу должен возвращаться сериализованный список всех объектов модели Post.

Подсказка
---------
Код аналогичен тому, что вы делали в прошлом уроке. 
Но написан он должен быть в объектно-ориентированном стиле.

В файл urls.py добавьте эндпоинт api/v1/posts/, 
который вызывает view-класс APIPost(). Не забудьте его импортировать.

Не стесняйтесь пользоваться кодом из Kittygram: 
там решалась очень похожая задача, и в листингах есть всё необходимое.
"""

# ------------------------------------------
# views.py
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class APIPost(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer =  PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------
# urls.py
from . import views
from django.urls import path

urlpatterns = [
    path('api/v1/posts/', views.APIPost.as_view()),
]

# ------------------------------------------
# serizlizers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post
