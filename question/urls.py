from django.urls import path

from . import views

urlpatterns = [
    path('', views.QuestionView.as_view(), name='question')
]
