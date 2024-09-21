from rest_framework import serializers
from erc_platform.models import ChainMember, Product, Contacts


class ChainMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChainMember
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"
