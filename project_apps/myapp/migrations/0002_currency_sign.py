# Generated by Django 4.1.4 on 2023-05-20 22:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="currency",
            name="sign",
            field=models.CharField(default="$", max_length=6, unique=True),
            preserve_default=False,
        ),
    ]
