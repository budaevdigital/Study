"""
Задача
-------
В Yatube API информация о дате создания поста передаётся по ключу pub_date. 

Добавьте в запросы информативности: сделайте так, чтобы пользователи 
API получали дату публикации поста в поле с именем publication_date.

Подсказка
----------
Используйте параметр source для переопределения названий полей сериализатора.

Поле publication_date в сериализаторе должно быть только «для чтения»: 
при создании поста берётся текущее время, передавать в запросе его не надо.
"""

# ------------------------------------------
# serizlizers.py
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    character_quantity = serializers.SerializerMethodField()
    publication_date = serializers.DateTimeField(source='pub_date', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'publication_date', 'character_quantity')

    def get_character_quantity(self, obj):
        return len(obj.text)
