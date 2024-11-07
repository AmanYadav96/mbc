from django.urls import path
from content.views import *

urlpatterns = [
    path('add/', ContentCreateView.as_view(), name='content_create'),
    path('view/', ContentListView.as_view(), name='content_list'),
    path('view/<uuid:content_id>/', ContentDetailView.as_view(), name='content_detail'),
    path('update/<uuid:content_id>/', ContentUpdateView.as_view(), name='content_update'),
    path('delete/<uuid:content_id>/', ContentDeleteView.as_view(), name='content_delete'),
]
