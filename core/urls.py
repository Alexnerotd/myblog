from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)



urlpatterns = [

    path('api/admin/accounts/', include('accounts.urls')),
    path('api/blog/', include('blog.urls')),

    path('api/admin/token/', TokenObtainPairView.as_view(), name='obtain-token'),
    path('api/admin/token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),

    path('api/user/', include('user.urls')),
]
