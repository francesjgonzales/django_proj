# Generated by Django 5.2.1 on 2025-06-03 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0005_menu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
