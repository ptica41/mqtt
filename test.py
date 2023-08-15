import pymysql
import datetime

data = [{'time': '14.08.2023 16:00:01', 'latitude': '53.178303', 'longitude': '45.008572', 'Температура': '23.73',
         'Влажность': '35.88',
         'Давление': '748.40', 'Уровень CO2': 0, 'Уровень NO2': 63, 'Уровень SO2': 0, 'Уровень CO': 1195,
         'Концентрация крупных частиц пыли (PM 10)': 5,
         'Концентрация мелкодисперсных частиц пыли (PM 2,5)': 5,
         'Концентрация ультрадисперсных частиц пыли (PM 1,0)': 4},
        {'time': '14.08.2023 16:00:21', 'latitude': '53.178299', 'longitude': '45.008579', 'Температура': '23.74',
         'Влажность': '35.86',
         'Давление': '748.40', 'Уровень CO2': 0, 'Уровень NO2': 63, 'Уровень SO2': 0, 'Уровень CO': 1203,
         'Концентрация крупных частиц пыли (PM 10)': 5,
         'Концентрация мелкодисперсных частиц пыли (PM 2,5)': 5,
         'Концентрация ультрадисперсных частиц пыли (PM 1,0)': 4},
        {'time': '14.08.2023 16:00:42', 'latitude': '53.178295', 'longitude': '45.008587', 'Температура': '23.75',
         'Влажность': '35.79', 'Давление': '748.40',
         'Уровень CO2': 0, 'Уровень NO2': 67, 'Уровень SO2': 0, 'Уровень CO': 1213,
         'Концентрация крупных частиц пыли (PM 10)': 5,
         'Концентрация мелкодисперсных частиц пыли (PM 2,5)': 5,
         'Концентрация ультрадисперсных частиц пыли (PM 1,0)': 4},
        {'time': '14.08.2023 16:01:02', 'latitude': '53.178291', 'longitude': '45.008595', 'Температура': '23.77',
         'Влажность': '35.70', 'Давление': '748.42',
         'Уровень CO2': 0, 'Уровень NO2': 65, 'Уровень SO2': 0, 'Уровень CO': 1185,
         'Концентрация крупных частиц пыли (PM 10)': 5,
         'Концентрация мелкодисперсных частиц пыли (PM 2,5)': 5,
         'Концентрация ультрадисперсных частиц пыли (PM 1,0)': 4}
        ]


def convert_datetime(a: str):  # преобразование строки в timedata
    t = datetime.datetime.strptime(a, '%d.%m.%Y %H:%M:%S')
    a = t.strftime('%Y-%m-%d %H:%M:%S')
    return a


start = convert_datetime(data[0]['time'])
end = convert_datetime(data[-1]['time'])

count = {'latitude': [59.178297, 4], 'longitude': [42.00858325, 4], 'Температура': [23.7475, 4],
         'Влажность': [35.807500000000005, 4], 'Давление': [748.405, 4], 'Уровень CO2': [0.0, 4],
         'Уровень NO2': [64.5, 4], 'Уровень SO2': [0.0, 4], 'Уровень CO': [1199.0, 4],
         'Концентрация крупных частиц пыли (PM 10)': [5.0, 4],
         'Концентрация мелкодисперсных частиц пыли (PM 2,5)': [5.0, 4],
         'Концентрация ультрадисперсных частиц пыли (PM 1,0)': [4.0, 4]}

con = pymysql.connect(host='localhost', user='root', password='Maksoft2023', database='test', charset='utf8mb4')
with con:
    cur = con.cursor()
    cur.execute(
        "SELECT id FROM point WHERE latitude BETWEEN {lat1} AND {lat2} AND longitude BETWEEN {lon1} AND {lon2} LIMIT 1".format(
            lat1=(round(count['latitude'][0], 6)) - 0.001, lat2=(round(count['latitude'][0], 6)) + 0.001,
            lon1=(round(count['longitude'][0], 6)) - 0.001, lon2=(round(count['longitude'][0], 6)) + 0.001))
    point_id = cur.fetchone()
    if not point_id:
        cur.execute(
            "INSERT INTO point (latitude, longitude) VALUES ({latitude}, {longitude})".format(
                latitude=round(count['latitude'][0], 6), longitude=round(count['longitude'][0], 6)))
        con.commit()
        cur.execute(
            "SELECT id FROM point WHERE latitude = {lat} AND longitude = {lon} LIMIT 1".format(
                lat=round(count['latitude'][0], 6), lon=round(count['longitude'][0], 6)))
        point_id = cur.fetchone()
    for i in count:
        if i == 'time' or i == 'latitude' or i == 'longitude':
            continue
        cur.execute("SELECT id FROM sensor WHERE name = '{name}'".format(name=i))
        sensor_id = cur.fetchone()
        print(start, end, point_id[0], sensor_id[0], round(count[i][0], 2))
        cur.execute(
            "INSERT INTO indication (start, end, point_id, sensor_id, value) VALUES ('{start}', '{end}', {point_id}, {sensor_id}, {value})".format(
                start=start, end=end, point_id=point_id[0], sensor_id=sensor_id[0], value=round(count[i][0], 2)))
        con.commit()
