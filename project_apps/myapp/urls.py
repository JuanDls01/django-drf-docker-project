from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.transaction_views import MoneyTransactionViewSet
from .views.currency_views import CurrencyViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"transactions", MoneyTransactionViewSet, basename="transaction")
router.register(r"currencies", CurrencyViewSet, basename="currency")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
