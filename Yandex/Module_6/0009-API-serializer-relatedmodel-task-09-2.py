"""
Задача
------
Добавьте к постам хештеги. Хештеги должны храниться в 
отдельной таблице в БД и быть связаны с постами отношением «многие-ко-многим».

При запросе постов должна возвращаться информация о всех связанных с конкретным 
постом хештегах, а при добавлении или обновлении поста нужно обеспечить возможность 
передавать названия хештегов списком прямо в теле запроса.

Без указания хештегов пост через API тоже должен создаваться.

Пример POST-запроса для создания поста с хештегами:
    {
        "text": "Текст для моего поста",
        "author": 1,
        "tag": [
            {"name": "хобби"},
            {"name": "личное"}
            ]
    } 

Подсказка
---------
Опишите сериализатор для модели Tag.

Опишите метод create() для сериализатора PostSerializer:

 - если поля tag нет в запросе — нужно создать пост из тех данных, которые были переданы;
 - если поле tag есть в запросе — нужно создать пост из переданных данных (без учёта поля tag), 
    добавить новые теги из переданного списка тегов в БД (если их там ещё нет),
    добавить в таблицу TagPost записи, которые свяжут новый пост с теми тегами,
    которые пришли в запросе или уже присутствуют в БД.

"""

# ------------------------------------------
# serizlizers.py
from rest_framework import serializers
from .models import Group, Post, Tag, TagPost


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        queryset=Group.objects.all(),
        slug_field='slug',
        required=False,
    )
    tag = TagSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group', 'tag')

    def create(self, validated_data):
        if 'tag' not in self.initial_data:
            post = Post.objects.create(**validated_data)
            return post
        tag = validated_data.pop('tag')
        post = Post.objects.create(**validated_data)
        for current_tag in tag:
            current, status = Tag.objects.get_or_create(**current_tag)
            TagPost.objects.create(tag=current, post=post)
        return post
