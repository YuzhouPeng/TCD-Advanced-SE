import requests
import json
import time
from functools import reduce
import redis

BIKE_API = 'https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=64a20cfe58b91e0c0acb1625055874a2b153c074'
BUS_API_STATIC = 'http://data.dublinked.ie/cgi-bin/rtpi/busstopinformation?stopid=&format=json'
BUS_API_REALTIME_TEMPLATE = 'https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid={}&format=json'
STOPS_ID = []
MIN_ROUTE_TO_FILTER =  5
r = redis.StrictRedis(host='redis', port=6379, db=0)  # TODO change it back to redis
TIME_FOR_SLEEP = 180


# r = requests.get(BIKE_API)
# @redisStore
def requestAllBikeRealtime(api=BIKE_API):
    # return like [
    #                 {'name': 'SMITHFIELD NORTH', 'latitude': 53.349562, 'longitude': -6.278198, 'bike_stands': 30, 'bike_available': 26,'last_update': None},
    #                  {'name': 'SMITHFIELD NORTH', 'latitude': 53.349562, 'longitude': -6.278198, 'bike_stands': 30, 'bike_available': 26, 'last_update': None}
    #              ]
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
    # return like [
    #               {'ID': '3', 'name': 'Parnell Square', 'latitude': '53.35230694', 'longitude': '-6.263783056', 'routes': ['120', '122'], 'last_update': None},
    #               {'ID': '4', 'name': 'Parnell Square', 'latitude': '53.35230694', 'longitude': '-6.263783056', 'routes': ['120', '122'], 'last_update': None},
    #               {'ID': '5', 'name': 'Parnell Square', 'latitude': '53.35230694', 'longitude': '-6.263783056', 'routes': ['120', '122'], 'last_update': None},
    #              ]
    def isInDublin(latitude, longitude):
        x = float(latitude)
        y = float(longitude)
        if x < 53.42214 and x > 53.226 and y > -6.446 and y < -6.04:
            return True
        return False

    def parseBus(dic):

        if dic['operators'][0]['name'] != 'bac' and dic['operators'][0]['name'] != 'BE':
            return None
        ID = dic['stopid']
        name = dic['fullname']
        latitude = dic['latitude']
        longitude = dic['longitude']
        routes = dic['operators'][0]['routes']
        last_updated = None  # TODO
        if not isInDublin(latitude, longitude):
            return None

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
    return str(stop_ID), {'ID': str(stop_ID),
                          'emmision_level': len(parsed_bus_status),
                          'comming_routes': parsed_bus_status}


def requestAllBusRealTime(stop_ID_list=STOPS_ID, template=BUS_API_REALTIME_TEMPLATE):
    # return like {
    #               '14': {'ID': '14', 'emmision_level': 19, 'comming_routes': [{'route': '16', 'direction': 'Inbound', 'source_time': '20/03/2018 20:53:06', 'arriveal_time': '20/03/2018 20:57:47', 'scheduled_time': '20/03/2018 21:06:00'}, {}] },
    #               '15': {'ID': '15', 'emmision_level': 19, 'comming_routes': [{'route': '16', 'direction': 'Inbound', 'source_time': '20/03/2018 20:53:06', 'arriveal_time': '20/03/2018 20:57:47', 'scheduled_time': '20/03/2018 21:06:00'}, {}] },
    #               '16': {'ID': '16', 'emmision_level': 19, 'comming_routes': [{'route': '16', 'direction': 'Inbound', 'source_time': '20/03/2018 20:53:06', 'arriveal_time': '20/03/2018 20:57:47', 'scheduled_time': '20/03/2018 21:06:00'}, {}] },
    #              }
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
        print('num of Top_ID are: ', len(STOPS_ID))
        # attention! here is a trap, default parameter will be set when initialized
        bus_realtime = requestAllBusRealTime(STOPS_ID)
        saveToRedis('BUS_REALTIME', bus_realtime)
        print('BUS_REALTIME writen')
        time.sleep(TIME_FOR_SLEEP)


def test():
    status0 = requestAllBikeRealtime()
    print(status0[0])
    status1 = requestAllBusStatic()
    print(status1[1])
    print(len(STOPS_ID))
    status2 = requestAllBusRealTime(STOPS_ID)
    print(type(status2))
    print(status2.keys())
    print(status2['14'])
    # status = requestAllBusStatic()
    #
    # print(status[1])
    # print(len(status))
    # print(len(STOPS_ID))


if __name__ == "__main__":
    runDaemon()
    # test()
