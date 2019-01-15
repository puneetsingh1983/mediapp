"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_swagger.views import get_swagger_view
from authentication import urls as user_urls
from organization import urls as organizatoin_urls
from userprofile import urls as profile_urls
from mobile_verification import urls as verify_urls

api_endpoints = get_swagger_view(title='Application API Endpoints')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/api-token-auth/', obtain_jwt_token),
    url(r'^api/v1/verify_jwt_token/', verify_jwt_token),
    url(r'^$', api_endpoints)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = urlpatterns + user_urls.urlpatterns + organizatoin_urls.urlpatterns + profile_urls.urlpatterns
urlpatterns = urlpatterns + verify_urls.urlpatterns
