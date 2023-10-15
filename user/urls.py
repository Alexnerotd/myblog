from django.urls import path
from .views import (Register, GetUserView, PutUserView, DeleteUserView,)



urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('user/', GetUserView.as_view(), name='get-user'),
    path('user/', PutUserView.as_view(), name='put-user'),
    path('user/', DeleteUserView.as_view(), name='delete-user'),
]
