# Generated by Django 4.1.6 on 2023-03-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_tager',
            field=models.BooleanField(null=True),
        ),
    ]
