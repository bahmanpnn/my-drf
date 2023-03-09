from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('', ArticleListApiView.as_view(), name='Article-list-api-view'),
    path('list-create', ArticleListCreateApiView.as_view(), name='Article-list-create-api-view'),
    path('<int:pk>', ArticleDetailView.as_view(), name='Article-detail-view'),
    path('users/', UserListApiView.as_view(), name='users-list-api-view'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail-view'),
]
