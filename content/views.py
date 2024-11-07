from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from content.serializers import ContentSerializer
from content.models import Content
from itsmbc.s3_config import upload_base64_file


# Create content
class ContentCreateView(GenericAPIView):
    serializer_class = ContentSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        url =upload_base64_file(request.data.get('vertical_poster'),"vertical-poster/")
        serializer.validated_data['vertical_poster'] = url
        url =upload_base64_file(request.data.get('horizontol_poster'),"horizontol-poster/")
        serializer.validated_data['horizontol_poster'] = url
        serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'message': 'Content created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

# List all content
class ContentListView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if not response.data:
            return Response({"message": "No Data Found!!"}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Content data retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

# Retrieve content by ID
class ContentDetailView(APIView):
    def get(self, request, content_id):
        try:
            content = Content.objects.get(content_id=content_id)
            serializer = ContentSerializer(content)
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Content data retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Content.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Content not found'
            }, status=status.HTTP_404_NOT_FOUND)

# Update content by ID
class ContentUpdateView(GenericAPIView):
    serializer_class = ContentSerializer

    def patch(self, request, content_id):
        try:
            content = Content.objects.get(content_id=content_id)
            serializer = self.get_serializer(content, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Content updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Content.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Content not found'
            }, status=status.HTTP_404_NOT_FOUND)

# Delete content by ID
class ContentDeleteView(APIView):
    def delete(self, request, content_id):
        try:
            content = Content.objects.get(content_id=content_id)
            content.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Content deleted successfully'
            }, status=status.HTTP_200_OK)
        except Content.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Content not found'
            }, status=status.HTTP_404_NOT_FOUND)
