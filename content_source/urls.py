from django.urls import path
from content_source.views import (
    SourceCreateView,
    SourceListView,
    SourceDetailView,
    SourceUpdateView,
    SourceDeleteView
)

urlpatterns = [
    path('add/', SourceCreateView.as_view(), name='create'),
    path('view/', SourceListView.as_view(), name='list'),
    path('view/<uuid:content_id>/', SourceDetailView.as_view(), name='detail'),
    path('update/<uuid:source_id>/', SourceUpdateView.as_view(), name='update'),
    path('delete/<uuid:source_id>/', SourceDeleteView.as_view(), name='delete'),
]
