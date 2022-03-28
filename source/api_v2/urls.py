from django.urls import path

from api_v2.views import ArticleListView, ArticleCreateView, ArticleDetailView

app_name = 'api_v2'

urlpatterns = [
    path("articles/", ArticleListView.as_view(), name='article'),
    path("articles/", ArticleCreateView.as_view(), name='article_create'),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name='article_detail'),

]
