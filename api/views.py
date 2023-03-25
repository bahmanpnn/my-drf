# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsStaffOrReadOnly, IsAuthor, IsSuperUserOrStaffReadOnly


# from rest_framework.authentication import BasicAuthentication

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['is_active', 'author__username', 'author__first_name', 'author__last_name']
    search_fields = ['title', 'content', 'author__username', 'author__first_name', 'author__last_name']
    ordering_fields = ['publish_date', 'is_active']
    ordering = ['-publish_date']

    # diffrence of ordering and ordering_fields is user can choose fields that want to order by that,
    # but ordering is set by default and user can't change that

    # this url is from search about is_active true and username of author is bahman!!
    # http://127.0.0.1:8000/rest-api/articles/?is_active=True&author__username=bahman

    # this url is for searching just by username that is mamad
    # http://127.0.0.1:8000/rest-api/articles/?is_active=true&author__username=mamad&author__first_name=&author__last_name=

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'destroy']:
            permission_classes = [IsStaffOrReadOnly, IsAuthor]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly, IsStaffOrReadOnly]
            # permission_classes = [IsStaffOrReadOnly]
        return [permission() for permission in permission_classes]


class ArticleListCreateApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsSuperUserOrStaffReadOnly,)

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


# def get_queryset(self):
#     queryset = Article.objects.all()
#
#     is_active = self.request.query_params.get('is_active')
#     if is_active is not None:
#         queryset = queryset.filter(is_active=is_active)
#
#     author = self.request.query_params.get('author')
#     if author is not None:
#         queryset = queryset.filter(author__username=author)  # author_name
#         # queryset = queryset.filter(author=author)  #author_id
#
#     return queryset

# class ArticleAuthorRelation(RetrieveAPIView):
#     queryset = get_user_model().objects.all()
#     # queryset = get_user_model().objects.filter(is_staff=True)
#     serializer_class = ArticleAuthorSerializer


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


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def delete(self, request):
#         request.auth.delete()
#         return Response({"msg": "delete"},status=204)
