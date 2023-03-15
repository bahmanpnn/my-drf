from django.contrib import admin
from django.urls import path, include

# from rest_framework.authtoken.views import obtain_auth_token
# from api.views import RevokeToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('rest-api/', include('api.urls')),
    # dj-rest-auth third party package
    path('rest-api/dj-rest-auth/', include('dj_rest_auth.urls')),
    # optional registration
    path('rest-api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))

    # this url is for our api that we create
    # remember that api-auth url was session login method
    # path('api-auth/', include('rest_framework.urls')),

    #     this url is post token for user
    # path('rest-api/api-token-auth/', obtain_auth_token),

    # this endpoint delete created token for target user and it use for logout user
    # path('rest-api/revoke/', RevokeToken.as_view(), name='revoke-token'),

]
