# Generated by Django 4.2.11 on 2024-04-10 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='game_genre',
            field=models.CharField(choices=[('action', 'Action'), ('adventure', 'Adventure'), ('puzzle', 'Puzzle'), ('role-playing', 'Role-playing'), ('simulation', 'Simulation'), ('strategy', 'Strategy'), ('sports', 'Sports'), ('mmo', 'MMO')], default='action', max_length=32),
        ),
    ]