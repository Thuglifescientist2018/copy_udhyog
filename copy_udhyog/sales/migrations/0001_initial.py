# Generated by Django 3.1.7 on 2021-03-11 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=4, max_digits=255, null=True)),
                ('quantity', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
                ('sold_to', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
