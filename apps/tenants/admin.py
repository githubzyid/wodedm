from django.contrib import admin
from .models import Client, Domain

# ============================================
# 平台管理后台（只管理租户和域名）
# ============================================
class PlatformAdminSite(admin.AdminSite):
    site_header = 'SaaS平台管理'
    site_title = '平台控制中心'
    index_title = '平台概览'

platform_admin = PlatformAdminSite(name='platform_admin')
platform_admin.register(Client)
platform_admin.register(Domain)

# ============================================
# 租户管理后台（只管理租户自己的内容）
# ============================================
class TenantAdminSite(admin.AdminSite):
    site_header = '租户管理'
    site_title = '租户控制台'
    index_title = '我的租户'

tenant_admin = TenantAdminSite(name='tenant_admin')
# 注意：不注册 Client 和 Domain
