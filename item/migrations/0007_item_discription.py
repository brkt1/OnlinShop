# Generated by Django 5.1.1 on 2024-09-28 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_rename_caragory_catagory'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discription',
            field=models.TextField(default=''),
        ),
    ]
