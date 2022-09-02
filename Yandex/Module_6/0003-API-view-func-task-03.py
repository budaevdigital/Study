"""
Задача
--------
Опишите view-функцию API api_posts(), которая будет работать с объектами модели Post и обрабатывать только GET- и POST-запросы:
- в ответ на GET-запрос функция должна возвращать queryset со всеми объектами модели Post;
- при POST-запросе функция должна создавать новый объект и возвращать его.

В файл urls.py добавьте эндпоинт api/v1/posts/, который вызывает view-функцию API api_posts.

Заранее предусмотрим в проекте возможность дальнейшего развития: будем версионировать API.
Начнём с первой версии: эндпоинты API будут выглядеть так: api/v1/....

В файле serializers.py подготовлен сериализатор PostSerializer. 


Подсказка
---------
В urls.py импортируйте view-функцию api_posts().
Чтобы PostSerializer мог обрабатывать коллекцию объектов, в конструкторе сериализатора укажите именованный аргумент many=True.
Примените методы сериализатора is_valid(), save() — и у вас всё получится!

"""
# ------------------------------------------
# views.py
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from rest_framework.response import Response
from .models import Post
from rest_framework import status


@api_view(['GET', 'POST'])
def api_posts(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# ------------------------------------------
# urls.py
from . import views
from django.urls import path

urlpatterns = [
    path('api/v1/posts/', views.api_posts),
]

# ------------------------------------------
# serizlizers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('text', 'author', 'pub_date')
        model = Post
