from django.db import models
from django.conf import settings
# Create your models here.
class Player(models.Model):
    score = models.IntegerField(default=0)
    position = models.CharField(max_length=50, null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        username = getattr(self.user, "username", "Anonymous")
        return f"Player {username} - Score: {self.score}"
    