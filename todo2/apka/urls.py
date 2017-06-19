from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^odmen/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.start),
]
