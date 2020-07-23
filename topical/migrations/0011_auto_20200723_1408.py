# Generated by Django 3.0.8 on 2020-07-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topical', '0010_ingredient_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(max_length=8192, null=True),
        ),
    ]