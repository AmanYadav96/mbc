from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from content.serializers import ContentSerializer
from content.models import Content
# from itsmbc.s3_config import upload_base64_file
from content.filter import ContentFilter
from django_filters.rest_framework import DjangoFilterBackend
from itsmbc.custom_paginations import CustomPagination


# Create content
class ContentCreateView(GenericAPIView):
    serializer_class = ContentSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # url =upload_base64_file(request.data.get('vertical_poster'),"vertical-poster/")
        # serializer.validated_data['vertical_poster'] = url
        # url =upload_base64_file(request.data.get('horizontol_poster'),"horizontol-poster/")
        # serializer.validated_data['horizontol_poster'] = url
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
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContentFilter
    pagination_class = CustomPagination
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

# import firebase_admin
# from firebase_admin import credentials, auth
# class GetAllUsersView(APIView):
#     def get(self, request):


# # Initialize Firebase Admin SDK
#      cred = credentials.Certificate("its-mbc-firebase-adminsdk-xfh4x-0fa1cb423e.json")  # Replace with the path to your service account key JSON file
#      firebase_admin.initialize_app(cred)

#      def fetch_all_users():
#         users = []
#     # Iterate over all users
#         page = auth.list_users()
#         while page:
#            for user in page.users:
#             users.append({
#                 "uid": user.uid,
#                 "email": user.email,
#                 "display_name": user.display_name,
#                 "phone_number": user.phone_number,
#                 "photo_url": user.photo_url,
#                 "disabled": user.disabled,
#                })
#         # Get the next page of users
#            page = page.get_next_page()

#         return users

# # Example usage:
#      all_users = fetch_all_users()
#      return Response({
#                 'status': status.HTTP_200_OK,
#                 'message': 'Content deleted successfully',
#                 'data': all_users
#             }, status=status.HTTP_200_OK)
