from django.urls import path
from home.views import (login_view, logout_view, index, about, contact, vote, result, dashboard_view,)
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("vote/", vote, name="vote"),
    path("result/", result, name="result"),

    # ✅ Authentication Routes (FIXED)
    path('login/', views.login_view, name='login'),  # Renamed from login to login_view
    path('logout/', views.logout_view, name='logout'),  # Ensure logout is using the correct view
    
    # ✅ Dashboard Route
    path("dashboard/", dashboard_view, name="dashboard"),
   
]


