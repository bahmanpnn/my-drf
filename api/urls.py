from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('', ArticleListApiView.as_view(), name='Article-list-api-view'),
    path('list-create', ArticleListCreateApiView.as_view(), name='Article-list-create-api-view'),
]
