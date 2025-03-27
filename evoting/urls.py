from django.contrib import admin
from django.urls import path, include  # ✅ Import include for app URLs

urlpatterns = [
    path("admin/", admin.site.urls),  # ✅ Django Admin panel route
    path("", include("home.urls")),   # ✅ Include all routes from home app
]