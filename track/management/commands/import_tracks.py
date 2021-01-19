import json
import re

from django.core.management import BaseCommand

from track.models import Artist, Track


class Command(BaseCommand):
    help = 'Import tracks from file to db'

    def handle(self, *args, **kwargs):

        with open('tracks.json') as json_file:
            tracks = json.load(json_file)

        artists_to_create_per_track = {}
        tracks_to_create = []

        for track in tracks:

            artist_names = map(
                str.strip,
                re.split(
                    '/|feat.|vs|&',
                    track['artist'],
                    flags=re.IGNORECASE
                )
            )
            artists = []
            for artist_name in artist_names:
                artist, created = Artist.objects.get_or_create(name=artist_name)
                artists.append(artist)

            artists_to_create_per_track[track['id']] = artists

            track['external_id'] = track.pop('id')
            track.pop('artist')

            tracks_to_create.append(Track(**track))

        Track.objects.bulk_create(tracks_to_create)

        # Add artists to tracks
        for track_ext_id, artists in artists_to_create_per_track.items():
            if artists:
                Track.objects.get(external_id=track_ext_id).artists.add(*artists)
