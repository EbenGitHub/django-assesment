# Generated by Django 5.0.4 on 2024-04-07 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0005_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
