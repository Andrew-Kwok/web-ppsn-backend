from django.urls import path

from .views import (
    RegistrationFormUploadView,
    RegistrationFormGetUUID,
    RegistrationFormGetDecision,
    RegistrationFormExport
)

urlpatterns = [
    path('upload/', RegistrationFormUploadView.as_view(), name="form-upload"),
    path("uuid/", RegistrationFormGetUUID.as_view(), name='get-uuid'),
    path("decision/<uuid:id>", RegistrationFormGetDecision.as_view(), name='get-decision'),
    path("export", RegistrationFormExport.as_view(), name='export'),
]
