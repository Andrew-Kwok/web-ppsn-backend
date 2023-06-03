from django.urls import path

from . import views

urlpatterns = [
    path('', views.NewsView.as_view(), name="news-all"),
    path('<int:id>', views.NewsView.as_view(), name="news-detail"),
]
