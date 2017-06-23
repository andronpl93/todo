from django.conf.urls import include, url
from django.contrib import admin
import apka

urlpatterns = [
    # Examples:
    # url(r'^$', 'todo2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apka.urls')),
    url(r'^archive/?', include('apka.urls'),{'archive':True}),
]
