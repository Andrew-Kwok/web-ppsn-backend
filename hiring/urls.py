from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.RegistrationFormUploadView.as_view(), name="form-upload"),
]
