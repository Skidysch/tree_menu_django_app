# Generated by Django 4.1.7 on 2023-03-23 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_menuitem_order_remove_menuitem_url_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['-id']},
        ),
    ]
