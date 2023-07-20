from rest_framework.response import Response
from rest_framework import views, status, pagination

from .models import News
from .serializers import NewsSerializer

import random

# Create your views here.
class NewsDetailAPIView(views.APIView):
    def get_object(self, news_id):
        try:
            return News.objects.get(pk=news_id)
        except News.DoesNotExist:
            return None

    def get(self, request, news_id):
        news = self.get_object(news_id)
        if not news:
            return Response({'error': 'News not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NewsSerializer(news)
        return Response(serializer.data)


class NewsPagination(pagination.PageNumberPagination):
    page_size_query_param = 'pageSize'
    max_page_size = 100
    default_page_size = 6

    page_query_param = 'page'
    default_page_number = 1

    def get_page_size(self, request):
        page_size = request.query_params.get(self.page_size_query_param)
        if page_size is None:
            return self.default_page_size
        return super().get_page_size(request)

    def get_page_number(self, request, paginator):
        page_number = request.query_params.get(self.page_query_param)
        if page_number is None:
            return self.default_page_number
        return super().get_page_number(request, paginator)


class NewsListByPaginationAPIView(views.APIView):
    def get(self, request):
        queryset = News.objects.order_by('-created_at')
        paginator = NewsPagination()

        result_page = paginator.paginate_queryset(queryset, request)
        serializer = NewsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    

class NewsOtherAPIView(views.APIView):
    def get(self, request, news_id):
        queryset = News.objects.exclude(pk=news_id).order_by('-created_at')

        result = []
        picked = set()
        for i in range(4):
            if len(queryset) == len(picked):
                break

            idx = 0
            l, r = 0, min(len(queryset) - 1, i * len(queryset) // 3)
            while idx in picked:
                idx = random.randint(l, r)
            picked.add(idx)
            result.append(queryset[idx])

        serializer = NewsSerializer(result, many=True)
        return Response(serializer.data)