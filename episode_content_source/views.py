from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from episode_content_source.serializers import EpisodesSerializer
from episode_content_source.models import Episodes
from episode_content_source.filter import EpisodeFilter
from django_filters.rest_framework import DjangoFilterBackend
from itsmbc.custom_paginations import CustomPagination
# Create Episode
class EpisodeCreateView(GenericAPIView):
    serializer_class = EpisodesSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'message': 'Episode created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

# List all Episodes
class EpisodeListView(ListAPIView):
    queryset = Episodes.objects.all()
    serializer_class = EpisodesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EpisodeFilter
    pagination_class = CustomPagination
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if not response.data:
            return Response({"message": "No Data Found!!"}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Episode data retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

# Retrieve Episode by ID
class EpisodeBySeasonView(APIView):
    def get(self, request, season_id):
        try:
            episode = Episodes.objects.get(season_id=season_id)
            serializer = EpisodesSerializer(episode, many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Episode data retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Episodes.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Episode not found'
            }, status=status.HTTP_404_NOT_FOUND)
            
class EpisodeBycontentView(APIView):
    def get(self, request, content_id):
        try:
            episode = Episodes.objects.get(content_id=content_id)
            serializer = EpisodesSerializer(episode, many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Episode data retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Episodes.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Episode not found'
            }, status=status.HTTP_404_NOT_FOUND)
            

# Update Episode by ID
class EpisodeUpdateView(GenericAPIView):
    serializer_class = EpisodesSerializer

    def patch(self, request, episode_id):
        try:
            episode = Episodes.objects.get(episode_id=episode_id)
            serializer = self.get_serializer(episode, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Episode updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Episodes.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Episode not found'
            }, status=status.HTTP_404_NOT_FOUND)

# Delete Episode by ID
class EpisodeDeleteView(APIView):
    def delete(self, request, episode_id):
        try:
            episode = Episodes.objects.get(episode_id=episode_id)
            episode.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Episode deleted successfully'
            }, status=status.HTTP_200_OK)
        except Episodes.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Episode not found'
            }, status=status.HTTP_404_NOT_FOUND)
