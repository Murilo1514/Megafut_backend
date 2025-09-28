from rest_framework import serializers
from .models import Team, TeamMember
from accounts.models import Player
from django.contrib.auth.models import User
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
    
    # username = serializers.CharField(write_only=True)
    # player = PlayerSerializer(read_only=True, source='player_id')
    # team = TeamSerializer(read_only=True, source='team_id')

    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())



    # class Meta:
    #     model = TeamMember
    #     fields = ['id', 'team', 'player', 'team_position', 'joined_at']

    class Meta:
        model = TeamMember
        fields = ['id', 'team', 'player', 'team_position', 'joined_at']

    # def create(self, validated_data):

    #     # username = validated_data.pop('username', None)
    #     # if username:
    #     #     try:
    #     #         user = User.objects.get(username=username)
    #     #         player = Player.objects.get(user=user)
    #     #     except Player.DoesNotExist:
    #     #         raise serializers.ValidationError("Usuário não encontrado.")
    #     #     validated_data['player'] = player

    #     player = self.initial_data.get('player', None)
    #     if player:
    #         try:
    #             # user = User.objects.get(username=username)
    #             player = Player.objects.get(id=player)
    #         except Player.DoesNotExist:
    #             raise serializers.ValidationError("Usuário não encontrado.")
    #         validated_data['player'] = player

    #     team = validated_data.get('team')

    #     if team:
    #         try:
    #             team = Team.objects.get(name=team)
    #             validated_data['team'] = team
    #         except Team.DoesNotExist:
    #             raise serializers.ValidationError("Time não encontrado.")
            
    #     team_member = TeamMember.objects.create(**validated_data)
    #     return team_member
