from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeamSerializer, TeamMemberSerializer
from .models import Team, TeamMember

# Create your views here.
class TeamView(APIView):
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            team = serializer.save()
            return Response(TeamSerializer(team).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.data:
            team_name = request.data.get('name')
            try:
                team = Team.objects.get(name=team_name)
                serializer = TeamSerializer(team)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Team.DoesNotExist:
                return Response({"error": "Team not found."}, status=status.HTTP_404_NOT_FOUND)
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamMemberView(APIView):
    def post(self, request):
        serializer = TeamMemberSerializer(data=request.data)
        if serializer.is_valid():
            team_member = serializer.save()
            return Response(TeamMemberSerializer(team_member).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if request.data:
            team_name = request.data.get('name')
            try:
                team = Team.objects.get(name=team_name)
                team_member = TeamMember.objects.get(team=team)
                serializer = TeamMemberSerializer(team_member)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Team.DoesNotExist:
                return Response({"error": "Team not found."}, status=status.HTTP_404_NOT_FOUND)

        team_members = TeamMember.objects.all()
        serializer = TeamMemberSerializer(team_members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # def get(self, request):
    #     if request.data:
    #         team_name = request.data.get('name')
    #         try:
    #             team = Team.objects.get(name=team_name)
    #             serializer = TeamSerializer(team)
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         except Team.DoesNotExist:
    #             return Response({"error": "Team not found."}, status=status.HTTP_404_NOT_FOUND)
    #     teams = Team.objects.all()
    #     serializer = TeamSerializer(teams, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)