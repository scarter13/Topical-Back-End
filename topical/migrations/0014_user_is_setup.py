# Generated by Django 3.0.8 on 2020-07-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topical', '0013_auto_20200724_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_setup',
            field=models.BooleanField(default=False),
        ),
    ]
