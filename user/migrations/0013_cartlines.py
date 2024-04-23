# Generated by Django 5.0.4 on 2024-04-23 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_description'),
        ('user', '0012_rename_product_cart_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('Cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_lines', to='user.cart')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]