from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from erc_platform.models import ChainMember, Product, Contacts
from users.models import User


class ChainMemberTestCase(APITestCase):
    """Тестирование модели ChainMember"""

    def setUp(self):
        """Создание пользователя и участников цепочки"""

        self.user = User.objects.create(email="admin@example.com")
        self.chain_member_1 = ChainMember.objects.create(
            name="Test Company 1",
            member=0,
            supplier=None,
            debt_to_supplier=0
        )
        self.chain_member_2 = ChainMember.objects.create(
            name="Test Company 2",
            member=0,
            supplier=self.chain_member_1,
            debt_to_supplier=0
        )
        self.product_1 = Product.objects.create(
            supplier=self.chain_member_1,
            name="Product 1",
            model="Model 1",
            release_date="2022-01-01"
        )
        self.product_2 = Product.objects.create(
            supplier=self.chain_member_2,
            name="Product 2",
            model="Model 2",
            release_date="2022-02-01"
        )

        self.contacts_1 = Contacts.objects.create(
            supplier=self.chain_member_1,
            email="test@example.com",
            country="Country 1",
            city="City 1",
        )
        self.contacts_2 = Contacts.objects.create(
            supplier=self.chain_member_2,
            email="test2@example.com",
            country="Country 2",
            city="City 2",
        )
        self.client.force_authenticate(user=self.user)

    def test_chain_member_create(self):
        """Тестирование создания участника цепочки"""

        url = reverse("erc_platform:chain_member_create")
        data = {
            "name": "Test Company 3",
            "member": 0,
            "supplier": self.chain_member_2.id,
            "debt_to_supplier": 0
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_chain_member_retrieve(self):
        """Тестирование получения информации о участнике цепочки"""

        url = reverse("erc_platform:chain_member_retrieve", args=(self.chain_member_1.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.chain_member_1.name)

    def test_chain_member_list(self):
        """Тестирование получения списка участников цепочки"""

        url = reverse("erc_platform:chain_member_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_chain_member_update(self):
        """Тестирование изменения информации о участнике цепочки"""

        url = reverse("erc_platform:chain_member_update", args=(self.chain_member_1.pk,))
        data = {
            "name": "Updated Test Company 1",
            "member": 0,
            "supplier": None,
            "debt_to_supplier": 0
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ChainMember.objects.get(pk=self.chain_member_1.pk).name, "Updated Test Company 1")

    def test_chain_member_delete(self):
        """Тестирование удаления участника цепочки"""

        url = reverse("erc_platform:chain_member_delete", args=(self.chain_member_1.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ChainMember.objects.all().count(), 1)


