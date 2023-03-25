# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from blog.models import Article


# class ArticleAuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['id', 'username', 'first_name', 'last_name']

# class AuthorUserNameField(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.username
#         # return value.first_name+' '+value.last_name


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    def get_article_author(self, obj):
        return {
            'username': obj.author.username,
            'first_name': obj.author.first_name,
            'last_name': obj.author.last_name,
        }

    author = serializers.SerializerMethodField('get_article_author')

    # author = serializers.CharField(source="author.username", read_only=True)
    # author = AuthorUserNameField(read_only=True)
    # author = serializers.HyperlinkedIdentityField(view_name='api:authors-detail')
    # author = ArticleAuthorSerializer()

    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ['created_date', 'updated']

    def validate_title(self, data):
        filter_list = ['php', 'js', 'laravel', 'javascript']
        for i in filter_list:
            if i in data:
                raise serializers.ValidationError('you can\'nt use another languages name!')
        return data

    def validate_slug(self, title, slug):
        if title == slug:
            raise serializers.ValidationError('you can\'nt use same title for slug!!')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
