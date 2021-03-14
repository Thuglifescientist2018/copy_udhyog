# Generated by Django 3.1.7 on 2021-03-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20210312_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='product_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='sold_to',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
