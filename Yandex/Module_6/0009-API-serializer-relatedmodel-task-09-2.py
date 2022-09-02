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

# ------------------------------------------
# models.py
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Введите текст поста'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        # оптимизация БД с помощью индексов
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
        # Аргумент upload_to указывает директорию,
        # в которую будут загружаться пользовательские файлы.
        upload_to='posts/',
        # Поле для картинки (необязательное)
        blank=True
    )
    # Связь будет описана через вспомогательную модель TagPost
    tags = models.ManyToManyField(Tag, through='TagPost', blank=True)

    class Meta:
        # переопределяем параметры фильтра и отображение имени
        # класса Post в ед. и мн. числе
        ordering = ('-pub_date'),
        verbose_name = 'Пост',
        verbose_name_plural = 'Посты'

    # для нормального отображения в списке
    # без этого метода, будет "Post object"
    # выведем 15 символов текста
    def __str__(self):
        return self.text[:15]


# В этой модели будут связаны id тегов и id поста
class TagPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag} {self.post}'