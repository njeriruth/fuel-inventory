# Generated by Django 3.1.2 on 2022-06-24 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20220624_0836'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Stock',
        ),
    ]