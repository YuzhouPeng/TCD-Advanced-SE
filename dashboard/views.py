from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
import redis


__cache = redis.StrictRedis(host='redis', port=6379)


@login_required
def home(request):
    return render(request, template_name='home.html')


@login_required
def bus_stations(request):
    str_ = __cache.get('BUS_STATIC').decode('utf-8')
    return HttpResponse(str_, content_type='application/json')


@login_required
def bus_realtime(request):
    str_ = __cache.get('BUS_REALTIME').decode('utf-8')
    return HttpResponse(str_, content_type='application/json')


@login_required
def bike_realtime(request):
    str_ = __cache.get('BIKE_REALTIME').decode('utf-8')
    return HttpResponse(str_, content_type='application/json')