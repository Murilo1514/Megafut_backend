from rest_framework import serializers
from .models import Team

# class PlayerSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(write_only=True)  
#     user = UserSerializer(read_only=True)  # exibe o usuário associado

#     class Meta:
#         model = Player
#         fields = ['id', 'score', 'position', 'username','user']

#     def create(self, validated_data):
#         username = validated_data.pop('username')
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             raise serializers.ValidationError("Usuário não encontrado.")
#         player = Player.objects.create(user=user, **validated_data)
#         return player
    

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        team = Team.objects.create(**validated_data)
        return team
    