from django.urls import path
from .views import Register, MyUserGETView

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('users/', MyUserGETView.as_view(), name='all-users'),
]
