from django_filters import FilterSet
from content.models import Content
import django_filters


class ContentFilter(FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Content
        fields = ['genre','network','content_type','title']