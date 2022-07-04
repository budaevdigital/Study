"""
Задача
------
При публикации одной из своих дневниковых записей пользователь @leo 
по ошибке вставил в текст поста свой почтовый индекс. 

В какой именно пост попала эта информация — он не помнит, но очень хочет удалить её из текста.

Помогите пользователю решить эту проблему и найти нужный пост через API. 
Почтовые индексы России состоят из 6 цифр. 

Такую последовательность в тексте легко обнаружить при помощи регулярного выражения.

Настройте поиск по текстам публикаций так, чтобы в качестве поисковых 
запросов можно было использовать регулярные выражения.

Подсказка
---------
Подключите бэкенд SearchFilter к нужному view-классу в приложении api.

Поведение поиска может быть уточнено путем добавления различных символов к полям в search_fields. 
Вам нужно использовать символ, который разрешит использовать регулярные выражения.
"""


# ------------------------------------------
# views.py
from rest_framework import filters


class PostViewSet(viewsets.ModelViewSet):     
	queryset = Post.objects.all()     
	serializer_class = PostSerializer     
	permission_classes = (AuthorOrReadOnly,)
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    # '$' - поиск с регулярным выражением в query parameters
    # GET http://.../api/v1/posts/?search=\d{6}
    search_fields = ('$text',)
