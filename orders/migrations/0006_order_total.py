# Generated by Django 4.1.4 on 2023-01-06 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_orders_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
