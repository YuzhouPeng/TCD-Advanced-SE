import requests
import json
import time
from functools import reduce
import redis


BIKE_API = 'https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=64a20cfe58b91e0c0acb1625055874a2b153c074'
BUS_API_STATIC = 'http://data.dublinked.ie/cgi-bin/rtpi/busstopinformation?stopid=&format=json'
BUS_API_REALTIME_TEMPLATE = 'https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid={}&format=json'
STOPS_ID = []
MIN_ROUTE_TO_FILTER = 6
r = redis.StrictRedis(host='redis', port=6379, db=0)
TIME_FOR_SLEEP = 300


# r = requests.get(BIKE_API)
# @redisStore
def requestAllBikeRealtime(api=BIKE_API):
    def parseBike(dic):
        name = dic["name"]
        latitude = dic['position']['lat']
        longitude = dic['position']['lng']
        bike_stands = dic['bike_stands']
        bike_available = dic['available_bikes']
        last_updated = None  # TODO

        if (not latitude) or (not longitude):
            #         return None
            pass  # TODO

        return {
            'name': name,
            'latitude': latitude,
            'longitude': longitude,
            'bike_stands': bike_stands,
            'bike_available': bike_available,
            'last_update': last_updated,
        }

    r = requests.get(api)
    if not r.ok:
        pass  # TODO
    bike_status_list = json.loads(r.content.decode("utf-8"))
    parsed_bike_status = map(parseBike, bike_status_list)
    parsed_bike_status = filter(lambda dic: dic is not None, parsed_bike_status)
    parsed_bike_status = list(parsed_bike_status)
    #     return a generator? or list?
    return parsed_bike_status


def requestAllBusStatic(api=BUS_API_STATIC):
    def parseBus(dic):

        if dic['operators'][0]['name'] != 'bac' and dic['operators'][0]['name'] != 'BE':
            return None
        ID = dic['stopid']
        name = dic['fullname']
        latitude = dic['latitude']
        longitude = dic['longitude']
        routes = dic['operators'][0]['routes']
        last_updated = None  # TODO
        if (not latitude) or (not longitude):
            #         return None
            pass  # TODO

        return {
            'ID': ID,
            'name': name,
            'latitude': latitude,
            'longitude': longitude,
            'routes': routes,
            'last_update': last_updated,
        }

    r = requests.get(api)
    if not r.ok:
        pass  # TODO
    bus_status = json.loads(r.content.decode("utf-8"))
    if bus_status['errorcode'] != '0':
        pass  # TODO
    bus_status_list = bus_status['results']
    parsed_bus_status = map(parseBus, bus_status_list)
    parsed_bus_status = filter(lambda dic: dic is not None, parsed_bus_status)
    parsed_bus_status = list(parsed_bus_status)

    global STOPS_ID
    STOPS_ID = filter(lambda dic: len(dic['routes']) > MIN_ROUTE_TO_FILTER, parsed_bus_status)
    STOPS_ID = list(map(lambda dic: dic['ID'], STOPS_ID))
    # print(STOPS_ID)
    return parsed_bus_status


def requestABusRealTime(stop_ID, template=BUS_API_REALTIME_TEMPLATE):
    def parseBus(dic):
        route = dic["route"]
        direction = dic['direction']
        source_time = dic["sourcetimestamp"]
        arrival_time = dic['arrivaldatetime']
        scheduled_time = dic["scheduledarrivaldatetime"]

        return {
            'route': route,
            'direction': direction,
            'source_time': source_time,
            'arriveal_time': arrival_time,
            'scheduled_time': scheduled_time
        }

    api = template.format(stop_ID)
    r = requests.get(api)
    if not r.ok:
        pass  # TODO
    bus_status = json.loads(r.content.decode('utf-8'))
    if bus_status['errorcode'] != '0':
        return str(stop_ID), None
    bus_status_list = bus_status['results']
    parsed_bus_status_list = map(parseBus, bus_status_list)
    parsed_bus_status = list(parsed_bus_status_list)
    #     print("got it", str(stop_ID))
    return str(stop_ID), parsed_bus_status


def requestAllBusRealTime(stop_ID_list=STOPS_ID, template=BUS_API_REALTIME_TEMPLATE):
    # print(stop_ID_list)
    bus_status_realtime_generator = map(requestABusRealTime, stop_ID_list)
    bus_status_realtime_generator = filter(lambda status: status[1] is not None, bus_status_realtime_generator)
    bus_status_realtime_generator = map(lambda status: {status[0]: status[1]}, bus_status_realtime_generator)
    #     return (bus_status_realtime_generator)
    bus_status_realtime_dic = reduce(lambda dic1, dic2: {**dic1, **dic2}, bus_status_realtime_generator)
    #     print(list(bus_status_realtime_generator))
    #     return bus_status_realtime_dic
    return bus_status_realtime_dic


def saveToRedis(key, value):
    value_json = json.dumps(value)
    r.set(key, value_json)


def runDaemon():
    bus_static = requestAllBusStatic()
    saveToRedis('BUS_STATIC', bus_static)
    print('BUS_STATIC written')
    while (True):
        bike_realtime = requestAllBikeRealtime()
        saveToRedis('BIKE_REALTIME', bike_realtime)
        print('BIKE_REALTIME written')
        print('STop_ID: \n', len(STOPS_ID))
        bus_realtime = requestAllBusRealTime(STOPS_ID) # attention! here is a trap, default parameter will be set when initialized
        saveToRedis('BUS_REALTIME', bus_realtime)
        print('BUS_REALTIME writen')
        time.sleep(TIME_FOR_SLEEP)


if __name__ == "__main__":
    runDaemon()
    # requestAllBikeRealtime()
