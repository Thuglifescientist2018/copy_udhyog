# Generated by Django 3.1.7 on 2021-03-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20210312_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]