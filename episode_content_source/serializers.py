from rest_framework import serializers
from episode_content_source.models import Episodes

class EpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields = '__all__'
