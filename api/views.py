# from django.shortcuts import render

from blog.models import Article
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView


class ArticleListApiView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleListCreateApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
