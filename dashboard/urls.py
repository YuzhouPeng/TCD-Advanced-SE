from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'dashboard'
urlpatterns = [
    url(r'^$', views.check_login),
    url(r'^logout', auth_views.logout),
    url(r'^login', auth_views.login, {'template_name': 'login.html'}),
    url(r'^api/bus_stations', views.bus_stations),
    url(r'^api/bus_realtime', views.bus_realtime),
    url(r'^api/bike_realtime', views.bike_realtime),
]