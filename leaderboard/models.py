from django.db import models
from django.utils import timezone

class Contestant(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=255)
    upvotes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class GameSession(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    contestant = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)

    def session_length(self):
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds() / 60  # minutes
        return 0

class Score(models.Model):
    game_session = models.ForeignKey(GameSession, on_delete=models.CASCADE)
    points = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

class Upvote(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
