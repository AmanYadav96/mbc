from django_filters import FilterSet
from episode_content_source.models import Episodes
import django_filters


class EpisodeFilter(FilterSet):
    
    class Meta:
        model = Episodes
        fields = ['season_number']