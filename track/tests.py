from django.test import TestCase
from rest_framework.reverse import reverse


class TrackViewTest(TestCase):

    fixtures = ['test_data.json']

    def test_fetch_single_track_good(self):
        response = self.client.get(
            reverse('track-detail', args=('1',)),
        )
        response_json = response.json()

        assert response.status_code == 200
        assert 'title' in response_json

    def test_create_new_track_good(self):
        response = self.client.post(
            '/api/tracks/',
            data={
                'external_id': 10000,
                'title': 'Lalalal',
                'duration': '300',
                'artists': '1',
                'last_play': '2018-05-17 15:23:20'
            }
        )
        assert response.status_code == 201

    def test_list_100_most_recent_tracks_good(self):
        response = self.client.get(
            reverse('track-list')
        )
        response_json = response.json()['results']
        last_track_played = response_json[0]
        second_last_track_played = response_json[1]

        assert response.status_code == 200
        assert last_track_played['last_play'] > second_last_track_played['last_play']
        assert len(response_json) <= 100

    def test_filter_tracks_by_name_good(self):
        response = self.client.get(
            reverse('track-list'), kwargs={
                'title': 'love'
            }
        )
        response_json = response.json()
        assert 'Love' in response_json['results'][0]['title']

    def test_list_artists_good(self):
        response = self.client.get(
            reverse('artist-list'),
        )
        response_json = response.json()

        assert response.status_code == 200

        first_artist = response_json[0]
        first_artist_keys = first_artist.keys()

        assert 'name' in first_artist_keys
        assert 'tracks_count' in first_artist_keys
        assert 'most_recent_played_track' in first_artist_keys
