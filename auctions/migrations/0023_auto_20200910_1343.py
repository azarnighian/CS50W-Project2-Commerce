# Generated by Django 3.0.8 on 2020-09-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20200910_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='auction',
            name='winner',
            field=models.CharField(blank=True, default=1, max_length=50),
            preserve_default=False,
        ),
    ]