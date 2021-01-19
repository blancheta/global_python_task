from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from track.models import Track, Artist


class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = ['title', 'artists', 'last_play', 'external_id', 'duration']


class ArtistSerializer(ModelSerializer):
    most_recent_played_track = serializers.CharField()
    tracks_count = serializers.IntegerField()

    class Meta:
        model = Artist
        fields = ['most_recent_played_track', 'tracks_count', 'name']
