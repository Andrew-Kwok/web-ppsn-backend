from django.urls import path

from .views import (
    NewsDetailAPIView,
    NewsListByPaginationAPIView,
    NewsOtherAPIView,
)

urlpatterns = [
    path('', NewsListByPaginationAPIView.as_view(), name="news-list"),
    path('<int:news_id>', NewsDetailAPIView.as_view(), name="news-detail"),
    path('other/<int:news_id>', NewsOtherAPIView.as_view(), name="news-other"),
]
