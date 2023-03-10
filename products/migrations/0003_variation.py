# Generated by Django 4.1.4 on 2023-01-06 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('price', models.FloatField()),
                ('price_additional', models.FloatField(blank=True, default=0.0)),
                ('price_discount', models.FloatField(blank=True, default=0.0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'variation',
                'verbose_name_plural': 'variations',
            },
        ),
    ]
