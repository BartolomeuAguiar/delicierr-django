# Generated by Django 4.1.4 on 2023-01-16 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_title_category_name_rename_title_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description_long',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_short',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
    ]