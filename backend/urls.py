"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='api/', permanent=True)),

    path('api/', include('api.urls')),
    path('api/news/', include('news.urls')),
    path('api/question/', include('question.urls')),
    path('api/hiring/', include('hiring.urls')),
    path('api/member/', include('member.urls')),
    path('api/voting/', include('voting.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

