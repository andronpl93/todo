from django.conf.urls import include, url
from django.contrib import admin
from apka import views


urlpatterns = [
    url(r'^$', views.start),
    url(r'^shuban-projects/$', views.projects),
    url(r'^shuban-tasks/$', views.tasks),
    url(r'^shuban-id/$', views.identificator),
    url(r'^shuban-add/$', views.add_edit),
    url(r'^shuban-add_pr/$', views.add_pr),
    url(r'^shuban-del-task/$', views.del_task),
    url(r'^shuban-del-pr/$', views.del_pr),
    url(r'^shuban-update_select/$', views.upd_select),

]
