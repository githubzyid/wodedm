from django.urls import path
from django.http import JsonResponse
from apps.tenants.admin import platform_admin

def health_check(request):
    return JsonResponse({'status': 'ok'})

def home(request):
    return JsonResponse({'message': 'Welcome to Django Multi-Tenant SaaS'})

urlpatterns = [
    path('admin/', platform_admin.urls),
    path('health/', health_check),
    path('', home),
]
