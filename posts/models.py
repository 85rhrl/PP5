from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    game_genre_choices = [
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('puzzle', 'Puzzle'),
        ('role-playing', 'Role-playing'),
        ('simulation', 'Simulation'),
        ('strategy', 'Strategy'),
        ('sports', 'Sports'),
        ('mmo', 'MMO')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_faqvmk', blank=True
    )
    game_genre = models.CharField(
        max_length=32, choices=game_genre_choices
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'