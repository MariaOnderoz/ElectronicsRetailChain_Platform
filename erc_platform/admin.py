from django.contrib import admin

from erc_platform.models import Product, Contacts, ChainMember


@admin.action
def clear_debt_to_supplier(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0)
    modeladmin.message_user(request, "Задолженность перед поставщиком успешно очищена.")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'name', 'model', 'release_date')
    search_fields = ('name',)
    list_filter = ('supplier', 'release_date')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'email', 'country', 'city', 'street', 'building_number')
    search_fields = ('email',)
    list_filter = ('city',)


@admin.register(ChainMember)
class ChainMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'member', 'supplier', 'debt_to_supplier', 'created_at')
    actions = [clear_debt_to_supplier]
    search_fields = ('name', 'supplier',)
    list_display_links = ['supplier']
