from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'leaderboard', leaderboardViewSet, basename='leaderboard')
router.register(r'hostels', HostelViewSet, basename='hostel')
router.register(r'missions', MissionViewSet, basename='mission')
router.register(r'participants', participantViewSet, basename='participant')
router.register(r'organisers', organiserViewSet, basename='organiser')

urlpatterns = [
    path('', include(router.urls)),
]
