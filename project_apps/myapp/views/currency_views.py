from rest_framework import viewsets
from config.pagination import CustomPagination
from ..models import Currency
from ..serializers.currency_serializers import CurrencySerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = CustomPagination
    search_fields = ["name"]
    ordering_fields = ["name"]
