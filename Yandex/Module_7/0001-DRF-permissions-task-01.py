"""
Задача
------
В приложении api опишите и примените пермишен, 
который не даст пользователю удалить или отредактировать чужие публикации.

Запрашивать список всех публикаций или отдельную публикацию может любой пользователь. 
Создавать новую публикацию может только аутентифицированный пользователь.

Подсказка
---------
- Безопасные запросы GET, OPTIONS и HEAD должны быть разрешены всем, даже анонимам.

- При запросах на изменение или удаление публикации проверьте, 
совпадает ли автор поста obj.author с автором запроса (с объектом request.user).

- В файле permissions.py опишите класс IsAuthorOrReadOnly. 
    Этот класс наследуется от BasePermission из пакета rest_framework.permissions.

- В теле класса переопределите метод has_object_permission(), 
    затем подключите класс IsAuthorOrReadOnly к необходимому view-классу публикаций.
"""

# ------------------------------------------
# permissions.py
from rest_framework.permissions import permissions


class IsAuthorOrReadOnly(permissions.BasePermissionMetaclass):
    # Определяет права на уровне объекта
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.is_authenticated:
            return True
        return obj.author == request.user