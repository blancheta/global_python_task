from django.db.models import Count, OuterRef, Subquery
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from track.models import Track, Artist
from track.serializers import TrackSerializer, ArtistSerializer


class TrackPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'


class TrackViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions for Track model.
    """

    queryset = Track.objects.all().order_by('-last_play')
    serializer_class = TrackSerializer
    pagination_class = TrackPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']


class ArtistListView(ListAPIView):

    """
    Provides a list view for Artist model.
    """

    def get_queryset(self):
        latest_track = Subquery(Track.objects.filter(
            artists__id=OuterRef("id"),
        ).values('title')[:1])

        qs = Artist.objects.annotate(
           most_recent_played_track=latest_track
        )
        qs = qs.annotate(
            tracks_count=Count('track')
        )
        return qs

    serializer_class = ArtistSerializer
