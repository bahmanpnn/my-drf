# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Article


class ArticleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name']


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedIdentityField(view_name='api:authors-detail')
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
