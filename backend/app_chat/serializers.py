from rest_framework import serializers
from .models import UserProfile, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'avatar', 'avatar_small', 'room')
