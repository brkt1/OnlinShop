# Generated by Django 5.1.1 on 2024-09-28 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0010_alter_item_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(default='', max_length=10),
        ),
    ]
