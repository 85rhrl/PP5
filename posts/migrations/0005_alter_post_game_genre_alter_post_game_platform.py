# Generated by Django 4.2.11 on 2024-04-10 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_game_platform_alter_post_game_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='game_genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('MMO', 'MMO'), ('Puzzle', 'Puzzle'), ('RPG', 'RPG'), ('Simulation', 'Simulation'), ('Strategy', 'Strategy'), ('Sports', 'Sports')], default='action', max_length=32),
        ),
        migrations.AlterField(
            model_name='post',
            name='game_platform',
            field=models.CharField(choices=[('Console', 'Console'), ('Mobile', 'Mobile'), ('PC', 'PC')], default='action', max_length=32),
        ),
    ]
