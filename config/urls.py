from django.urls import path, include
from apps.tenants.admin import tenant_admin

urlpatterns = [
    path('admin/', tenant_admin.urls),
    path('api/', include('apps.api.urls')),
]
