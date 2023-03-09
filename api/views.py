# from django.shortcuts import render
from django.contrib.auth.models import User

from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ArticleListApiView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleListCreateApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# we can set every method to some class and set some url->url/1/delete =>articleDetailView(destroy)
class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'


# user
class UserListApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
