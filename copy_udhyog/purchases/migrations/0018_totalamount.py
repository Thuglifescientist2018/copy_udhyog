# Generated by Django 3.1.7 on 2021-04-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0017_remove_purchases_pending_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=255, null=True)),
            ],
        ),
    ]
