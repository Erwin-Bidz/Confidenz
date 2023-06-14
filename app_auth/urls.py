from django.urls import path
from app_auth.views import login_confidenz

urlpatterns = [
    path('login/', login_confidenz, name="login_confidenz"),
]
