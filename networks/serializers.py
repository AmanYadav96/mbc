from rest_framework import serializers
from networks.models import Network

class NetworkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Network
        fields = ['name','description','network_image']
        