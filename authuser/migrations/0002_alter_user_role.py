# Generated by Django 5.0.4 on 2024-04-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('football player', 'Football Player'), ('coach', 'Coach'), ('agent', 'Agent'), ('admin', 'Admin')], default='football player', max_length=25),
        ),
    ]
