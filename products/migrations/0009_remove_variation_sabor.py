# Generated by Django 4.1.4 on 2023-01-16 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_variation_sabor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='sabor',
        ),
    ]
