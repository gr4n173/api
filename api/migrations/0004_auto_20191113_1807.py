# Generated by Django 2.2.7 on 2019-11-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_housedetails_power_consumption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housedetails',
            name='power_consumption',
            field=models.IntegerField(),
        ),
    ]
