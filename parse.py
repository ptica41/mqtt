import random
import time
import json
import logging
import datetime
from copy import deepcopy

import pymysql
from paho.mqtt import client as mqtt_client

broker = '192.168.65.65'
port = 1883
topic = 'test'
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'test'
password = 'test'

data_list = []  # словарь для парсинга данных
data_dict = {}  # словарь для парсинга данных
count = 0  # индикатор для записи значений, начиная со 2-го полученного
t = datetime.datetime.now()


# logging.basicConfig(level=logging.DEBUG, filename='client.log', filemode='a',
#                     format='%(asctime)s - %(name)s : %(levelname)s - %(message)s')
#
# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %dn", rc)

    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    global count, data_dict, data_list, t
    count = 0  # индикатор для записи значений, начиная со 2-го полученного
    data_list = []  # список для парсинга данных
    data_dict = {}  # словарь для парсинга данных
    t = datetime.datetime.now()
    client.subscribe([(topic, 2), ])
    client.on_message = on_message
    # with open('data.txt', mode='at') as f:
    #     f.write(f"{datetime.datetime.now()} - {data_list}\n\n")


def on_message(client, userdata, msg):
    global count, data_dict, data_list, t
    t = datetime.datetime.now()
    data = msg.payload.decode()
    with open('log.txt', mode='at') as f:
        f.write(f"{datetime.datetime.now()} - Received `{data}` from `{msg.topic}` topic\n")
    print(f"Received `{data}` from `{msg.topic}` topic")
    # data.append(json.loads(data))
    # if count == 0:
    #     count = 1
    #     return
    # data_dict.update({'time': data['GLONASS'][0] + ' ' + data['GLONASS'][1]})
    # data_dict.update({'latitude': data['GLONASS'][2], 'longitude': data['GLONASS'][3]})
    # data_dict.update(
    #     {'Температура': data['BME280'][0], 'Влажность': data['BME280'][1], 'Давление': data['BME280'][2]})
    # data_dict.update({'Уровень CO2': data['CO2'][0]})
    # data_dict.update({'Уровень NO2': data['NO2'][0]})
    # data_dict.update({'Уровень SO2': data['SO2'][0]})
    # data_dict.update({'Уровень CO': data['CO'][0]})
    # data_dict.update({'Концентрация крупных частиц пыли (PM 10)': data['DUST'][0],
    #                   'Концентрация мелкодисперсных частиц пыли (PM 2,5)': data['DUST'][1],
    #                   'Концентрация ультрадисперсных частиц пыли (PM 1,0)': data['DUST'][2]})
    # data_list.append(deepcopy(data_dict))
    # data_dict.clear()



def convert_datetime(a: str):  # преобразование строки в timedata
    t = datetime.datetime.strptime(a, '%d.%m.%Y %H:%M:%S')
    a = t.strftime('%Y-%m-%d %H:%M:%S')
    return a


def to_base(data: list):  # запись в БД
    start = convert_datetime(data[0]['time'])
    end = convert_datetime(data[-1]['time'])
    count = {'latitude': [0, 0],
             'longitude': [0, 0],
             'Температура': [0, 0],
             'Влажность': [0, 0],
             'Давление': [0, 0],
             'Уровень CO2': [0, 0],
             'Уровень NO2': [0, 0],
             'Уровень SO2': [0, 0],
             'Уровень CO': [0, 0],
             'Концентрация крупных частиц пыли (PM 10)': [0, 0],
             'Концентрация мелкодисперсных частиц пыли (PM 2,5)': [0, 0],
             'Концентрация ультрадисперсных частиц пыли (PM 1,0)': [0, 0]}

    for i in data:
        for j in count:
            if i[j] != 0:
                count[j][0] += float(i[j])
                count[j][1] += 1

    for i in count:
        count[i][0] /= count[i][1]

    with open('count.txt', mode='at') as f:
        f.write(f"{datetime.datetime.now()} - {count}\n\n")

    con = pymysql.connect(host='localhost', user='root', password='Maksoft2023', database='mqtt', charset='utf8mb4')
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT id FROM point WHERE latitude BETWEEN {lat1} AND {lat2} AND longitude BETWEEN {lon1} AND {lon2} LIMIT 1".format(
                lat1=count['latitude'][0] - 0.001, lat2=count['latitude'][0] + 0.001,
                lon1=count['longitude'][0] - 0.001, lon2=count['longitude'][0] + 0.001))
        point_id = cur.fetchone()
        if not point_id:
            cur.execute(
                "INSERT INTO point (latitude, longitude) VALUES ({latitude}, '{longitude}')".format(
                    latitude=count['latitude'][0], longitude=count['longitude'][0]))
            con.commit()
            cur.execute(
                "SELECT id FROM point WHERE latitude = {lat} AND longitude = {lon} LIMIT 1".format(
                    lat=count['latitude'][0], lon=count['longitude'][0]))
            point_id = cur.fetchone()
        for i in count:
            if i == 'time' or i == 'latitude' or i == 'longitude':
                continue
            cur.execute("SELECT id FROM sensor WHERE name = '{name}'".format(name=i))
            sensor_id = cur.fetchone()
            cur.execute(
                "INSERT INTO indication (start, end, point_id, sensor_id, value) VALUES ({start}, '{end}', {point_id}, {sensor_id}, {value})".format(
                    start=start, end=end, point_id=point_id[0], sensor_id=sensor_id[0], value=count[i][0]))
            con.commit()


if __name__ == '__main__':
    while True:
        try:
            client = connect_mqtt()
            subscribe(client)
            client.loop_start()
            while (datetime.datetime.now() - t).total_seconds() < 3*60:
                # print(int((datetime.datetime.now() - t).total_seconds()))
                client.loop_stop()
            print(datetime.datetime.now(), ' – Таймаут получения данных')
            # to_base(data)
        except TimeoutError:
            print(datetime.datetime.now(), ' – Таймаут подключения, повторная попытка через 5 минут')
            time.sleep(60 * 5)

