"""
Задача
------
Создайте сериализатор для модели Post в проекте Yatube.

Импортируйте фреймворк rest_framework.serializers и на 
основе класса serializers.ModelSerializer создайте класс PostSerializer.

В PostSerializer опишите class Meta с двумя полями: fields и model.

В fields перечислите поля для вывода текста, автора и даты публикации. 
Сериализатор не должен обрабатывать поле id из модели Post.

В поле model укажите модель, с которой будет связан сериализатор

Подсказка
---------
Проверьте, правильно ли импортированы необходимые классы.

В поле fields перечислите поля модели, 
необходимые для работы сериализатора: ('text', 'author', 'pub_date').

В поле model укажите имя модели, с которой должен работать сериализатор, — Post.

Модель Post:
    class Post(models.Model):
        text = models.TextField(
            verbose_name='Текст поста',
            help_text='Введите текст поста'
        )
        pub_date = models.DateTimeField(
            verbose_name='Дата публикации',
            auto_now_add=True,
            db_index=True)
        author = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='posts',
            verbose_name='Автор'
        )
        group = models.ForeignKey(
            Group,
            on_delete=models.SET_NULL,
            related_name='group',
            blank=True,
            null=True,
            verbose_name='Группа',
            help_text='Выберите группу'
        )
        image = models.ImageField(
            verbose_name='Картинка',
            help_text='Вставьте картинку размером до 5 Мб',
            upload_to='posts/',
            blank=True
        )
"""

import rest_framework.serializers

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('text', 'author', 'pub_date')