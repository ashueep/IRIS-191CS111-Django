# Generated by Django 3.2.3 on 2021-05-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Club', '0004_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Item Name'),
        ),
    ]
