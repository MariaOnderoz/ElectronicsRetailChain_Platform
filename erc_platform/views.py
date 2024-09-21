from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from erc_platform.models import ChainMember, Product, Contacts
from erc_platform.serializer import ChainMemberSerializer, ProductSerializer, ContactsSerializer
from users.permissions import IsActive
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ChainMemberCreateAPIView(CreateAPIView):
    """Создание члена цепочки поставок"""

    queryset = ChainMember.objects.all()
    serializer_class = ChainMemberSerializer
    permission_classes = (IsActive,)


class ChainMemberListAPIView(ListAPIView):
    """Список всех членов цепочки поставок"""

    queryset = ChainMember.objects.all()
    serializer_class = ChainMemberSerializer
    permission_classes = (IsActive,)


class ChainMemberRetrieveAPIView(RetrieveAPIView):
    """Детальная информация о члене цепочки поставок"""

    queryset = ChainMember.objects.all()
    serializer_class = ChainMemberSerializer
    permission_classes = (IsActive,)


class ChainMemberUpdateAPIView(UpdateAPIView):
    """Редактирование члена цепочки поставок"""

    queryset = ChainMember.objects.all()
    serializer_class = ChainMemberSerializer
    permission_classes = (IsActive,)

    def perfom_update(self, serializer):
        if "debt_to_supplier" in serializer.validate_data:
            serializer.validate_data.pop("debt_to_supplier")
            raise Exception("Обновление поля запрещено")
        super().perform_update(serializer)


class ChainMemberDestroyAPIView(DestroyAPIView):
    """Удаление члена цепочки поставок"""

    queryset = ChainMember.objects.all()
    serializer_class = ChainMemberSerializer
    permission_classes = (IsActive,)


class ProductViewSet(ModelViewSet):
    """Контроллер продукта"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ContactsViewSet(ModelViewSet):
    """Контроллер контактов поставщика"""

    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['country']
    search_fields = ['country']
    permission_classes = (IsActive,)
