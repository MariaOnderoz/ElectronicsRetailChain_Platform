from django.db import models

NULLABLE = {'blank': True, 'null': True}


class ChainMember(models.Model):
    """Модель члена цепочки поставок"""

    member_choices = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=255, verbose_name="Название организации")
    member = models.CharField(choices=member_choices, verbose_name="Звено сети")
    supplier = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name="Поставщик", **NULLABLE)
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Задолженность перед поставщиком", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")


class Product(models.Model):
    """Модель продукта"""

    supplier = models.ForeignKey(ChainMember, on_delete=models.CASCADE, verbose_name="Поставщик")
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    model = models.CharField(max_length=255, verbose_name="Модель продукта")
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Contacts(models.Model):
    """Модель контактов поставщика"""

    supplier = models.ForeignKey(ChainMember, on_delete=models.CASCADE, verbose_name="Поставщик")
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=50, verbose_name="Улица")
    building_number = models.CharField(max_length=50, verbose_name="Номер дома")

    def __str__(self):
        return f"{self.email} - {self.country}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
