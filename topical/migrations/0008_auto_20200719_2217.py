# Generated by Django 3.0.8 on 2020-07-19 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topical', '0007_auto_20200718_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='upc',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
