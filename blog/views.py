from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Article


class ArticleList(ListView):
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(is_active=True)
