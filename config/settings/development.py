"""
Development settings
"""
from .base import *

DEBUG = True

# Allow all localhost variations for development
ALLOWED_HOSTS = [
    'saas.jiaxiani.xyz',
    '.saas.jiaxiani.xyz',  # 匹配所有子域名，如 tenant1.saas.jiaxiani.xyz
    'localhost',
    '127.0.0.1',
]

# Development-specific CORS settings
CORS_ALLOW_ALL_ORIGINS = True

# Add development tools
INSTALLED_APPS += [
    'django_extensions',  # Provides shell_plus, runserver_plus, and other dev utilities
]

# Show SQL queries in development
LOGGING['loggers']['django.db.backends'] = {
    'handlers': ['console'],
    'level': 'DEBUG',
    'propagate': False,
}

CSRF_TRUSTED_ORIGINS = [
    'http://tenant1.saas.jiaxiani.xyz:56455',
    'http://saas.jiaxiani.xyz:56455',
]
