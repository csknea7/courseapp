# Generated by Django 5.0.4 on 2024-04-22 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_category_destination_category'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='category_table',
        ),
        migrations.AlterModelTable(
            name='destination',
            table='destination_table',
        ),
    ]