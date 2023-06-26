from django.urls import path

from . import views

urlpatterns = [
    path('', views.NewsListByPaginationAPIView.as_view(), name="news-list"),
    path('<int:news_id>', views.NewsDetailAPIView.as_view(), name="news-detail"),
]
