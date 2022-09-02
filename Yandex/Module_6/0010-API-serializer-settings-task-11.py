"""
Задача
-------
Владельцы интернет-ресурсов покупают готовые статьи на биржах; 
стоимость зависит от количества символов в тексте. 

Настройте Yatube API так, чтобы в ответ на GET-запрос поста 
(или списка постов) вместе с информацией о посте возвращалось 
дополнительное поле character_quantity.

В этом поле верните количество символов в запрошенных публикациях.

Подсказка
---------
Для поля character_quantity установите тип SerializerMethodField.

Значение поля character_quantity вычислите в методе 
get_character_quantity().
"""

# ------------------------------------------
# serizlizers.py
from rest_framework import serializers
from .models import Post, Group


class PostSerializer(serializers.ModelSerializer):
    character_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'character_quantity')

    def get_character_quantity(self, obj):
        return len(obj.text)
