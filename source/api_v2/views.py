from rest_framework.response import Response
from rest_framework.views import APIView

from api_v2.serializers import ArticleSerializer
from webapp.models import Article


class ArticleListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Article.objects.all()
        serializer = ArticleSerializer(objects, many=True)
        return Response(serializer.data)


class ArticleCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            article = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class ArticleDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
