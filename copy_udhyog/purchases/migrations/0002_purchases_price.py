# Generated by Django 3.1.7 on 2021-03-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=255, null=True),
        ),
    ]
