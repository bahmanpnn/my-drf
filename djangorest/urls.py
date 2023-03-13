from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('rest-api/', include('api.urls')),
    # this url is for our api that we create
    # path('api-auth/', include('rest_framework.urls')),
    # remember that api-auth url was session login method
    path('rest-api/api-token-auth/', obtain_auth_token),
    #     this url is post token for user
]
