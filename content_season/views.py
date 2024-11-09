from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from content_season.serializers import SeasonSerializer
from content_season.models import Season
# from itsmbc.s3_config import upload_base64_file

# Create season
class SeasonCreateView(GenericAPIView):
    serializer_class = SeasonSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # url =upload_base64_file(request.data.get('vertical_p'),"vertical-poster/")
        # serializer.validated_data['vertical_poster'] = url
        serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'message': 'Season created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

# List all seasons
class SeasonListView(ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if not response.data:
            return Response({"message": "No Data Found!!"}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Season data retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

# Retrieve season by ID
class SeasonDetailView(APIView):
    def get(self, request, content_id):
        try:
            season = Season.objects.filter(content_id=content_id)
            serializer = SeasonSerializer(season , many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Season data retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Season.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Season not found'
            }, status=status.HTTP_404_NOT_FOUND)

# Update season by ID
class SeasonUpdateView(GenericAPIView):
    serializer_class = SeasonSerializer

    def patch(self, request, season_id):
        try:
            season = Season.objects.get(season_id=season_id)
            serializer = self.get_serializer(season, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Season updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Season.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Season not found'
            }, status=status.HTTP_404_NOT_FOUND)

# Delete season by ID
class SeasonDeleteView(APIView):
    def delete(self, request, season_id):
        try:
            season = Season.objects.get(season_id=season_id)
            season.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Season deleted successfully'
            }, status=status.HTTP_200_OK)
        except Season.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Season not found'
            }, status=status.HTTP_404_NOT_FOUND)
