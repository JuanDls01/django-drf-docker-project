from rest_framework import serializers
from ..models import MoneyTransaction


class MoneyTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyTransaction
        exclude = ("location_from", "location_to")
