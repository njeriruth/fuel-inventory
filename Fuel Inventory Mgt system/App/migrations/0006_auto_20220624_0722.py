# Generated by Django 3.1.2 on 2022-06-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_delete_fuel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel', models.CharField(max_length=200)),
                ('eprice', models.FloatField()),
                ('mrice', models.FloatField()),
                ('expense', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]