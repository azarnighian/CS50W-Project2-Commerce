# Generated by Django 3.0.8 on 2020-08-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200826_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='winner',
            field=models.IntegerField(default=None),
        ),
    ]