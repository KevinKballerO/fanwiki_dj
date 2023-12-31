# Generated by Django 4.2.6 on 2023-11-05 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='is_live',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='first_appearance',
            field=models.CharField(max_length=300),
        ),
    ]
