# Generated by Django 4.2.7 on 2023-11-23 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_character_is_live_character_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('air_date', models.DateField()),
                ('episode', models.CharField(max_length=255)),
                ('characters', models.ManyToManyField(related_name='episodes', to='api.character')),
            ],
        ),
    ]
