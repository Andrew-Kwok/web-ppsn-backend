from django.urls import path

from . import views

urlpatterns = [
    path('', views.HelloWorldView.as_view(), name='hello_world'),
    path('question', views.QuestionView.as_view(), name='question')
]
