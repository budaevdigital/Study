"""
Задача
-------
Настройте API для Yatube так, чтобы при запросе постов возвращалась 
информация о группе, в которой опубликован пост. 
Данные о группе должны возвращаться в виде значения её поля slug.

Добавьте возможность при создании или изменении поста через API
опционально указывать группу, передавая в теле запроса поле slug.

Подсказка
----------
Чтобы получить значение slug из объекта поста, при переопределении
поля group в сериализаторе назначьте ему тип SlugRelatedField.

Подробности о работе с полями типа SlugRelatedField описаны в шпаргалке.

При переопределении поля group в сериализаторе, укажите для него параметр queryset.

Чтобы сделать поле сериализатора необязательным — укажите для него параметр required=False.
"""

# ------------------------------------------
# serizlizers.py
from rest_framework import serializers
from .models import Post, Group


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        queryset=Group.objects.all(),
        slug_field='slug',
        required=False,
    )

    
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group',)
        model = Post