# Generated by Django 5.1.1 on 2024-09-28 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_item_telegram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='telegram',
        ),
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='item',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='telegram_link',
            field=models.URLField(blank=True),
        ),
    ]
