from django.urls import path
from networks.views import (
    NetworkCreateView,
    NetworkListView,
    NetworkDetailView,
    NetworkUpdateView,
    NetworkDeleteView
)

urlpatterns = [
    path('add/', NetworkCreateView.as_view(), name='network_create'),
    path('view/', NetworkListView.as_view(), name='network_list'),
    path('view/<uuid:network_id>/', NetworkDetailView.as_view(), name='network_detail'),
    path('update/<uuid:network_id>/', NetworkUpdateView.as_view(), name='network_update'),
    path('delete/<uuid:network_id>/', NetworkDeleteView.as_view(), name='network_delete'),
]
