from django.http import JsonResponse
from django.views import View

from .models import Sensor, Indication, Point
from .config import STATUS
import json

# STATUS = {"Уровень CO2": [6, 10],
#           "Уровень NO2": [6, 10],
#           "Уровень SO2": [4, 10],
#           "Уровень CO": [4, 8],
#           "Концентрация крупных частиц пыли (PM 10)": [2, 3],
#           "Концентрация мелкодисперсных частиц пыли(PM 2, 5)": [2, 3],
#           "Концентрация ультрадисперсных частиц пыли (PM 1,0)": [2, 3]
#           }  # диапазоны состояний статуса


# class Marks(View):
#     def get(self, request):
#         status = ["normal", "warning", "critical"]
#         body = json.loads(request.body.decode('utf-8'))
#         start = body['filter']['dateTime']['start']
#         end = body['filter']['dateTime']['end']
#         indications = Indication.objects.filter(start__gt=start,
#                                                 end__lt=end).values()  # получение данных по заданным параметрам
#         indications_serialized = []  # сериализованный список словарей с нужными данными
#
#         for i in indications:
#             count = 0
#             latitude = list(Point.objects.filter(id=i["point_id"]).values("latitude"))[0]["latitude"]
#             longitude = list(Point.objects.filter(id=i["point_id"]).values("longitude"))[0]["longitude"]
#
#             for serial in indications_serialized:  # проверка на вхождении точки в список
#                 if serial["id"] == i["point_id"]:
#                     count += 1
#
#             if not count:  # если точки нет в списке - добавляем
#                 indications_serialized.append({"id": i["point_id"],
#                                                "coordinates": {"latitude": float(latitude),
#                                                                "longitude": float(longitude)},
#                                                "status": i["status"]})
#
#             for serial in indications_serialized:  # исправляем статус
#                 if serial["id"] == i["point_id"] and serial["status"] == status[0] and i["status"] != status[0]:
#                     serial["status"] = i["status"]
#                 elif serial["id"] == i["point_id"] and serial["status"] == status[1] and i["status"] == status[2]:
#                     serial["status"] = i["status"]
#
#         data = {
#             "marks": indications_serialized
#         }
#         return JsonResponse(data)


class Marks(View):
    def get(self, request):
        body = json.loads(request.body.decode('utf-8'))
        start = body['filter']['dateTime']['start']
        end = body['filter']['dateTime']['end']
        indications = Indication.objects.filter(start__gt=start,
                                                end__lt=end).values()  # получение данных по заданным параметрам
        indications_serialized = []  # сериализованный список словарей с нужными данными

        for i in indications:  # запись всех нужных данных, кроме правильного статуса
            count = 0
            latitude = list(Point.objects.filter(id=i["point_id"]).values("latitude"))[0]["latitude"]
            longitude = list(Point.objects.filter(id=i["point_id"]).values("longitude"))[0]["longitude"]
            if not i["status"]:  # определение и добавление в БД правильного статуса
                s = Indication.objects.get(id=i["id"])
                i["status"] = s.set_status

            for serial in indications_serialized:  # проверка на вхождении точки в список
                if serial["id"] == i["point_id"]:
                    count += 1

            if not count:  # если точки нет в списке - добавляем
                indications_serialized.append({"id": i["point_id"],
                                               "coordinates": {"latitude": float(latitude),
                                                               "longitude": float(longitude)},
                                               "status": "normal"})

        # for serial in indications_serialized:  # запись правильного статуса
        #     values = Indication.objects.filter(start__gt=start, end__lt=end,
        #                                        point_id=serial["id"]).values()
        #     count_dict = {}  # словарь с количеством вхождений одинаковых датчиков в точке. Для подсчета среднего арифметического
        #     values_list = []  # список словарей с данными по датчикам
        #
        #     for i in values:
        #         count = 1
        #         name = list(Sensor.objects.filter(id=i["sensor_id"]).values("name"))[0]["name"]
        #
        #         for val in values_list:  # если датчик уже есть в списке - прибавляем значение показателя и увеличиваем счетчик в словаре
        #             if val["name"] == name:
        #                 count += 1
        #                 val.update({"value": val["value"] + i["value"]})
        #                 count_dict.update({name: count_dict[name] + 1})
        #
        #         if count == 1:  # если датчика не оказалось в списке - добавляем данные
        #             values_list.append(
        #                 {"name": name, "value": i["value"], "status": "normal"})
        #             count_dict.update({name: 1})
        #
        #     for val in values_list:  # делим сумму показателей датчика на количество вхождений
        #         for count in count_dict:
        #             if val["name"] == count:
        #                 val["value"] /= count_dict[count]
        #
        #     for val in values_list:  # записываем статус в зависимости от среднего арифметического
        #         for i in STATUS:
        #             if val["name"] == i and STATUS[i][0] <= val["value"] <= STATUS[i][1]:
        #                 val["status"] = "warning"
        #             elif val["name"] == i and val["value"] > STATUS[i][1]:
        #                 val["status"] = "critical"
        #         if val["status"] == "critical":
        #             serial["status"] = "critical"
        #         elif val["status"] == "warning" and serial["status"] != "critical":
        #             serial["status"] = "warning"

        data = {
            "marks": indications_serialized
        }
        return JsonResponse(data)


class SensorReadings(View):
    def get(self, request, id):
        body = json.loads(request.body.decode('utf-8'))
        start = body['filter']['dateTime']['start']
        end = body['filter']['dateTime']['end']
        indications = Indication.objects.filter(start__gt=start, end__lt=end,
                                                point_id=id).values()  # получение данных по заданным параметрам

        indications_serialized = []  # сериализованный список словарей с нужными данными
        count_dict = {}  # словарь с количеством вхождений одинаковых датчиков в точке. Для подсчета среднего арифметического

        for i in indications:
            count = 1  # счетчик количества вхождений
            name = list(Sensor.objects.filter(id=i["sensor_id"]).values("name"))[0]["name"]
            unit = list(Sensor.objects.filter(id=i["sensor_id"]).values("unit"))[0]["unit"]
            if not i["status"]:  # определение и добавление в БД правильного статуса
                s = Indication.objects.get(id=i["id"])
                i["status"] = s.set_status

            for serial in indications_serialized:  # если датчик уже есть в списке - прибавляем значение показателя и увеличиваем счетчик в словаре
                if serial["name"] == name:
                    count += 1
                    serial.update({"value": serial["value"] + i["value"]})
                    count_dict.update({name: count_dict[name] + 1})

            if count == 1:  # если датчика не оказалось в списке - добавляем данные
                indications_serialized.append(
                    {"name": name, "value": i["value"], "unit": unit, "status": "normal"})
                count_dict.update({name: 1})

        for serial in indications_serialized:  # делим сумму показателей датчика на количество вхождений
            for count in count_dict:
                if serial["name"] == count:
                    serial["value"] /= count_dict[count]

        # for serial in indications_serialized:  # записываем значения уровней в зависимости от среднего арифметического
        #     for val in STATUS:
        #         if serial["name"] == val and STATUS[val][0] <= serial["value"] <= STATUS[val][1]:
        #             serial["status"] = "warning"
        #         elif serial["name"] == val and serial["value"] > STATUS[val][1]:
        #             serial["status"] = "critical"

        data = {
            "sensorReadings": indications_serialized
        }
        return JsonResponse(data)


# class SensorReadings(View):
#     def get(self, request, id):
#         status = ["normal", "warning", "critical"]
#         body = json.loads(request.body.decode('utf-8'))
#         start = body['filter']['dateTime']['start']
#         end = body['filter']['dateTime']['end']
#         # point_id = list(Indication.objects.filter(id=id).values("point_id"))[0]["point_id"]
#         indications = Indication.objects.filter(start__gt=start, end__lt=end, point_id=id).values()
#         indications_serialized = []
#         for i in indications:
#             name = list(Sensor.objects.filter(id=i["sensor_id"]).values("name"))[0]["name"]
#             unit = list(Sensor.objects.filter(id=i["sensor_id"]).values("unit"))[0]["unit"]
#             indications_serialized.append(
#                 {"name": name, "value": i["value"], "unit": unit, "status": i["status"]})
#         data = {
#             "sensorReadings": indications_serialized
#         }
#         return JsonResponse(data)

class HistorySensorReadings(View):
    def get(self, request, id):
        body = json.loads(request.body.decode('utf-8'))
        start = body['filter']['dateTime']['start']
        end = body['filter']['dateTime']['end']
        indications = Indication.objects.filter(start__gt=start, end__lt=end,
                                                point_id=id).order_by('-start').values()  # получение данных по заданным параметрам

        indications_serialized = []  # сериализованный список словарей с нужными данными
        data_list = []  # список словарей без объединения замеров по времени

        for i in indications:
            name = list(Sensor.objects.filter(id=i["sensor_id"]).values("name"))[0]["name"]
            unit = list(Sensor.objects.filter(id=i["sensor_id"]).values("unit"))[0]["unit"]
            if not i["status"]:
                s = Indication.objects.get(id=i["id"])
                i["status"] = s.set_status

            data_list.append({"dateTime": {"start": i["start"], "end": i["end"]}, "sensorReadings": [
                {"name": name, "value": i["value"], "unit": unit, "status": i["status"]}]})

        for i in data_list:
            for j in data_list:
                if i["dateTime"] == j["dateTime"] and i != j:
                    i["sensorReadings"].append(j["sensorReadings"][0])
                    j["dateTime"] = "on_delete"


        for i in data_list:
            if i["dateTime"] != "on_delete":
                indications_serialized.append(i)

        data = {
            "groups": indications_serialized
        }
        return JsonResponse(data)
