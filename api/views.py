# from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsStaffOrReadOnly, IsAuthor, IsSuperUserOrStaffReadOnly
from rest_framework.authentication import BasicAuthentication


# class ArticleListApiView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# # we can set every method to some class and set some url->url/1/delete =>articleDetailView(destroy)
# class ArticleDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsStaffOrReadOnly, IsAuthor)
#     lookup_field = 'pk'


# with this model_view_set we can set 2views(article_list+article_detail_list) to 1 view set that handle them
# we must set permissions for (retrieve and update and destroy) for article and others need to set default permissions
# that we set in settings file
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'destroy']:
            permission_classes = [IsStaffOrReadOnly, IsAuthor]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly, IsStaffOrReadOnly]
        return [permission() for permission in permission_classes]


class ArticleListCreateApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# user
# class UserListApiView(ListCreateAPIView):
#     # queryset = User.objects.all()
#     def get_queryset(self):
#         print(self.request.user)
#         print(self.request.auth)
#         return User.objects.all()
#
#     serializer_class = UserSerializer
#     permission_classes = [IsSuperUserOrStaffReadOnly]
#     # permission_classes = (IsSuperUserOrStaffReadOnly,)
#     # authentication_classes = (BasicAuthentication,)
#
#
# class UserDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUserOrStaffReadOnly,)
#     # permission_classes = [IsAdminUser]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)

# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def delete(self, request):
#         request.auth.delete()
#         return Response({"msg": "delete"},status=204)
