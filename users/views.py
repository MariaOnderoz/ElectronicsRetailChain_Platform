from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from users.models import User
from users.serializer import UserSerializer
from users.permissions import IsActive


class UserCreateAPIView(CreateAPIView):
    """Создание пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    """Список всех пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsActive,)


class UserRetrieveAPIView(RetrieveAPIView):
    """Детальная информация о пользователе"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsActive,)


class UserUpdateAPIView(UpdateAPIView):
    """Редактирование информации о пользователе"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsActive,)


class UserDestroyAPIView(DestroyAPIView):
    """Удаление пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsActive,)
