from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = 'api'
router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('articles', ArticleViewSet, basename='articles')

# urlpatterns = router.urls==> we can use this one or urlpatterns=[] that i used bottom

urlpatterns = [
    path('', include(router.urls)),
    path('article-create/', ArticleListCreateApiView.as_view()),
    # path('authors/<int:pk>/', ArticleAuthorRelation.as_view(), name='authors-detail'),
]

# urlpatterns = [
# path('', ArticleListApiView.as_view(), name='Article-list-api-view'),
# path('list-create', ArticleListCreateApiView.as_view(), name='Article-list-create-api-view'),
# path('<int:pk>', ArticleDetailView.as_view(), name='Article-detail-view'),
# path('users/', UserListApiView.as_view(), name='users-list-api-view'),
# path('users/<int:pk>', UserDetailView.as_view(), name='user-detail-view'),
# ]
