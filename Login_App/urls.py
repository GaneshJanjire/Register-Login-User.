from django.urls import path
from .views import RegisterUser, LoginUser, ChangePassword

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('change_password/', ChangePassword.as_view(), name='change-password'),
]
