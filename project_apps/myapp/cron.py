from datetime import datetime

from project_apps.myapp.models import MoneyTransaction, Currency


def my_cron_job():
    print("hola", datetime.now())
    currency = Currency.objects.first()
    transaction = MoneyTransaction(
        description="Transacción creada en cron", amount=1, currency=currency
    )
    transaction.save()
