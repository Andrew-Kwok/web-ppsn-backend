from django.urls import path

from .views import (
    RegistrationFormUploadView,
    RegistrationFormGetUUID,
    RegistrationFormGetDecision,
    DecisionList,
    # RegistrationFormExport
)

urlpatterns = [
    path('upload/', RegistrationFormUploadView.as_view(), name="form-upload"),
    path("uuid/", RegistrationFormGetUUID.as_view(), name='get-uuid'),
    path("decision/<uuid:id>", RegistrationFormGetDecision.as_view(), name='get-decision'),
    path("decision-sc3n/list/", DecisionList.as_view(), name='get-decision-list'),
    # path("export", RegistrationFormExport.as_view(), name='export'),
]
