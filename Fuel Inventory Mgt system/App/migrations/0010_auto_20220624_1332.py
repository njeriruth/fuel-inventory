# Generated by Django 3.1.2 on 2022-06-24 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20220624_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculation',
            name='expense',
        ),
        migrations.RemoveField(
            model_name='calculation',
            name='netprofit',
        ),
        migrations.RemoveField(
            model_name='calculation',
            name='purchase',
        ),
        migrations.RemoveField(
            model_name='calculation',
            name='sales',
        ),
    ]
