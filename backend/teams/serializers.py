from rest_framework import serializers
from .models import Team, TeamMember
from accounts.models import Player
from accounts.serializers import PlayerSerializer

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        team = Team.objects.create(**validated_data)
        return team

class TeamMemberSerializer(serializers.ModelSerializer):
    # TODO: Make create method to only accept ids instead of nested objects
    
    username = serializers.CharField(write_only=True)
    player = PlayerSerializer(read_only=True, source='player_id')
    
    class Meta:
        model = TeamMember
        fields = ['id', 'team', 'player', 'team_position', 'joined_at']

    def create(self, validated_data):

        username = validated_data.pop('username', None)
        if username:
            try:
                player = Player.objects.get(username=username)
            except Player.DoesNotExist:
                raise serializers.ValidationError("Usuário não encontrado.")
            validated_data['player_id'] = player.id

        team_member = TeamMember.objects.create(**validated_data)
        return team_member
