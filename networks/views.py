from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from networks.serializers import NetworkSerializer
from networks.models import Network
from itsmbc.s3_config import upload_base64_file

# Create network
class NetworkCreateView(GenericAPIView):
    serializer_class = NetworkSerializer
    
    def post(self, request):
        if Network.objects.filter(name=request.data.get('name')).count()>=1:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Network already exists'
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # folder_name = 'network-image/'
        # url =upload_base64_file(request.data.get('network_image'),folder_name)
        # serializer.validated_data['network_image'] = url
        
        serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'message': 'Network created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

# List all networks
class NetworkListView(ListAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if not response.data:
            return Response({"message": "No Data Found!!"}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Network data retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

# Retrieve network by ID
class NetworkDetailView(APIView):
    def get(self, request, network_id):
        try:
            network = Network.objects.get(network_id=network_id)
            serializer = NetworkSerializer(network)
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Network data retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Network.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Network not found'
            }, status=status.HTTP_404_NOT_FOUND)

# Update network by ID
class NetworkUpdateView(GenericAPIView):
    serializer_class = NetworkSerializer

    def patch(self, request, network_id):
        try:
            network = Network.objects.get(network_id=network_id)
            serializer = self.get_serializer(network, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Network updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Network.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Network not found'
            }, status=status.HTTP_404_NOT_FOUND)

# Delete network by ID
class NetworkDeleteView(APIView):
    def delete(self, request, network_id):
        try:
            network = Network.objects.get(network_id=network_id)
            network.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Network deleted successfully'
            }, status=status.HTTP_200_OK)
        except Network.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Network not found'
            }, status=status.HTTP_404_NOT_FOUND)
