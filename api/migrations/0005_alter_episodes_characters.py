# Generated by Django 4.2.7 on 2023-11-23 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_episodes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodes',
            name='characters',
            field=models.ManyToManyField(to='api.character'),
        ),
    ]
