# Generated by Django 2.1.5 on 2020-06-05 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200604_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='ItemTypeId',
            new_name='itemTypeId',
        ),
    ]