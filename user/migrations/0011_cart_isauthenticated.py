# Generated by Django 5.0.4 on 2024-04-23 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_cart_isauthenticated'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='isAuthenticated',
            field=models.BooleanField(default=False),
        ),
    ]
