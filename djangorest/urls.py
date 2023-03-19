from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView
from django.views.generic import TemplateView
from rest_framework_simplejwt import views as jwt_views

# from rest_framework.authtoken.views import obtain_auth_token
# from api.views import RevokeToken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('rest-api/', include('api.urls')),
    # path('rest-api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('rest-api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # dj-rest-auth third party package
    # i dont know why token/verify that is in jwt urlpatterns of this packages doesn't work!!
    path('rest-api/dj-rest-auth/', include('dj_rest_auth.urls')),
    # optional registration
    path('rest-api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # they are 2 path of django-allauth urls that we must override them to use and don't have error
    path('rest-api/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    # this is not in course So I added it for having better experience to log in and logout in rest templates
    # path('rest-api/rest-framework/', include('rest_framework.urls')),

    # it didn't work :( try again next time you have time
    # path(
    #     'rest-api/account-email-verification-sent/', TemplateView.as_view(template_name="email_verify.html"),
    #     name='account_email_verification_sent',
    # ),

    # this url is for our api that we created
    # remember that api-auth url was session login method
    # path('api-auth/', include('rest_framework.urls')),

    # -------------------------------
    #     this url is post token for user
    # path('rest-api/api-token-auth/', obtain_auth_token),

    # this endpoint delete created token for target user and it use for logout user
    # path('rest-api/revoke/', RevokeToken.as_view(), name='revoke-token'),

]
