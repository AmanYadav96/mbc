from django.urls import path
from content_season.views import *

urlpatterns = [
    path('add/', SeasonCreateView.as_view(), name='season_create'),
    path('view/', SeasonListView.as_view(), name='season_list'),
    path('view/<uuid:content_id>/', SeasonDetailView.as_view(), name='season_detail'),
    path('update/<uuid:season_id>/', SeasonUpdateView.as_view(), name='season_update'),
    path('delete/<uuid:season_id>/', SeasonDeleteView.as_view(), name='season_delete'),
]
