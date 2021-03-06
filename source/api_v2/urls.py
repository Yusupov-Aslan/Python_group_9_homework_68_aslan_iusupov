from django.urls import path

from api_v2.views import (ArticleListView,
                          ArticleCreateView,
                          ArticleDetailView,
                          ArticleUpdateView,
                          ArticleDeleteView)

app_name = 'api_v2'

urlpatterns = [
    path("articles/", ArticleListView.as_view(), name='article'),
    path("articles/create/", ArticleCreateView.as_view(), name='article_create'),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name='article_detail'),
    path("articles/<int:pk>/update/", ArticleUpdateView.as_view(), name='article_update'),
    path("articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name='article_delete'),
]
