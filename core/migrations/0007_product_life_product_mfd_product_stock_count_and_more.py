# Generated by Django 5.1.6 on 2025-02-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_remove_productimages_user_productimages_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="life",
            field=models.CharField(default="100 Days", max_length=100),
        ),
        migrations.AddField(
            model_name="product",
            name="mfd",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="stock_count",
            field=models.CharField(default="10", max_length=100),
        ),
        migrations.AddField(
            model_name="product",
            name="type",
            field=models.CharField(default="Organic", max_length=100),
        ),
    ]
