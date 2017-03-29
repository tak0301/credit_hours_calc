from django.conf.urls import url

from . import views

app_name = 'calc'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<activity_id>[0-9]+)/activity/$', views.activity, name='activity')
]
