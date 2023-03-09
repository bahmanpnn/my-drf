from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleList(ListView):
    # model = Article
    # template_name = 'blog/article_list.html'

    # #if template name equal to class name with (_) it doesn't need to set template name
    # ArticleList =>article_list.html

    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(is_active=True)


class ArticleDetail(DetailView):
    # arg=url/1,bahman,...
    # kwarg=url/pk=1,author=bahman,.....
    context_object_name = 'article'

    def get_object(self, queryset=None):
        return get_object_or_404(Article.objects.filter(is_active=True),
                                 pk=self.kwargs.get('pk')
                                 )
