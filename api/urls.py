from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # YOUR PATTERNS
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Debug Toolbar:
    path("__debug__/", include("debug_toolbar.urls")),
    # Admin Panel:
    path('admin/', admin.site.urls),
    # Apps
    path('library/', include('library.urls')),
    path('user/', include('user.urls'))
    
]
