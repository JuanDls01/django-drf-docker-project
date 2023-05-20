from datetime import date
from django.db import models


class Location(models.Model):
    name: str = models.CharField(max_length=25, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "location"


class Currency(models.Model):
    name: str = models.CharField(max_length=25, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "currency"


class Categories(models.Model):
    name: str = models.CharField(max_length=25, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "categories"


class MoneyTransaction(models.Model):
    description: str = models.CharField(max_length=40)
    amount: float = models.FloatField()
    currency: Currency = models.ForeignKey(Currency, on_delete=models.RESTRICT)
    location_from: Location = models.ForeignKey(
        Location,
        related_name="location_from",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
    location_to: Location = models.ForeignKey(
        Location,
        related_name="location_to",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
    generation_date: date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.description}"

    class Meta:
        db_table = "money_transaction"
