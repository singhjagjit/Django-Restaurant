# Generated by Django 2.1.5 on 2020-06-05 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200604_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='itemId',
            new_name='item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderNum',
        ),
        migrations.AddField(
            model_name='order',
            name='itemType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.ItemType'),
        ),
    ]