# Generated by Django 5.0.4 on 2024-04-22 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_customuser_options_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='isAuthenticated',
        ),
    ]