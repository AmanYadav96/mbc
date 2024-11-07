from django.urls import path
from episode_content_source.views import (
    EpisodeCreateView,
    EpisodeListView,
    EpisodeBySeasonView,
    EpisodeUpdateView,
    EpisodeDeleteView,
    EpisodeBycontentView
)

urlpatterns = [
    path('add/', EpisodeCreateView.as_view(), name='create'),
    path('view/', EpisodeListView.as_view(), name='list'),
    path('Episode-by-season-view/<uuid:season_id>/', EpisodeBySeasonView.as_view(), name='detail'),
    path('Episode-by-content-view/<uuid:content_id>/', EpisodeBycontentView.as_view(), name='detail'),
    path('update/<uuid:episode_id>/', EpisodeUpdateView.as_view(), name='update'),
    path('delete/<uuid:episode_id>/', EpisodeDeleteView.as_view(), name='delete'),
]
