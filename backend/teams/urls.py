from django.urls import path

from .views import TeamView, TeamMemberView

urlpatterns = [
    path('teams/', TeamView.as_view(), name='team'),
    path('team-members/', TeamMemberView.as_view(), name='team-member'),
]

