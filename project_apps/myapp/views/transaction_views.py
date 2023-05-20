from rest_framework import viewsets
from config.pagination import CustomPagination
from ..models import MoneyTransaction
from ..serializers.transactions_serializers import MoneyTransactionsSerializer


class MoneyTransactionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = MoneyTransaction.objects.all()
    serializer_class = MoneyTransactionsSerializer
    pagination_class = CustomPagination
    search_fields = ["description", "amount", "currency", "generation_date"]
    ordering_fields = ["description", "amount", "currency", "generation_date"]
