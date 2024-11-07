from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from content_source.serializers import SourceSerializer
from content_source.models import Source

# Create Source
class SourceCreateView(GenericAPIView):
    serializer_class = SourceSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'message': 'Source created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

# List all Sources
class SourceListView(ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if not response.data:
            return Response({"message": "No Data Found!!"}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Source data retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

# Retrieve Source by ID
class SourceDetailView(APIView):
    def get(self, request, content_id):
        try:
            source = Source.objects.get(content_id=content_id)
            serializer = SourceSerializer(source)
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Source data retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Source.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Source not found'
            }, status=status.HTTP_404_NOT_FOUND)

# Update Source by ID
class SourceUpdateView(GenericAPIView):
    serializer_class = SourceSerializer

    def patch(self, request, source_id):
        try:
            source = Source.objects.get(source_id=source_id)
            serializer = self.get_serializer(source, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Source updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Source.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Source not found'
            }, status=status.HTTP_404_NOT_FOUND)

# Delete Source by ID
class SourceDeleteView(APIView):
    def delete(self, request, source_id):
        try:
            source = Source.objects.get(source_id=source_id)
            source.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Source deleted successfully'
            }, status=status.HTTP_200_OK)
        except Source.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Source not found'
            }, status=status.HTTP_404_NOT_FOUND)
