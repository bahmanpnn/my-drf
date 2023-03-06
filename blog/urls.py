from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='article_list')
]
