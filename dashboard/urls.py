from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'dashboard'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout', auth_views.logout),
    path('bus_stations', views.bus_stations, name="bus_stations"),
    path('bus_realtime', views.bus_realtime, name="bus_realtime"),
    path('bike_realtime', views.bike_realtime, name="bike_realtime"),
]