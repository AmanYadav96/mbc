from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.generic import TemplateView


# 
get_schema_view = get_schema_view(
    openapi.Info(
        title="StartBusiness ",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',
         include([path('api_schema', get_schema_view.as_view(), name="api_schema"),path('docs/', TemplateView.as_view(template_name='docs.html',extra_context={'schema_url': 'api_schema'}), name='docs'),
             path('content/',include('content.urls')),
             path('content-season/',include('content_season.urls')),
             path('network/',include('networks.urls')),
             path('episode-source/',include('episode_content_source.urls')),
             path('content-source/',include('content_source.urls')),
             
            
             
             
       ]))
]
