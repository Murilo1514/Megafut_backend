from django.db import models

# Create your models here.
class Player(models.Model):
    score = models.IntegerField(default=0)
    position = models.CharField(max_length=50, null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        username = getattr(self.user, "username", "Anonymous")
        return f"Player {username} - Score: {self.score}"
    

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Team {self.name}"