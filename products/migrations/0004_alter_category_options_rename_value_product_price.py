# Generated by Django 4.1.4 on 2023-01-06 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_variation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='value',
            new_name='price',
        ),
    ]