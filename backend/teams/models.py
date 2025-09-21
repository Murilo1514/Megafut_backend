from django.db import models
from backend.accounts.models import Player

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Team {self.name}"


class TeamMember(models.Model):
    team = models.ForeignKey(Team, related_name='members', on_delete=models.CASCADE)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)  # Assuming user IDs are integers
    role = models.CharField(max_length=50, blank=True, null=True)  # e.g., 'admin', 'member'

    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.user_id} in Team {self.team.name}"