from django.urls import path
from .views import Register, MyUserGETPOSTView, MyUserPUTView, MyUserDELETEView

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('users/', MyUserGETPOSTView.as_view(), name='all-users'),
    path('users/update/<int:pk>/', MyUserPUTView.as_view(), name="update-users"),
    path('users/delete/<int:pk>/', MyUserDELETEView.as_view(), name="delete-users"),

]
