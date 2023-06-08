class SensorReadings(View):
    def get(self, request, id):
        body = json.loads(request.body.decode('utf-8'))
        start = body['filter']['dateTime']['start']
        end = body['filter']['dateTime']['end']
        # point_id = list(Indication.objects.filter(id=id).values("point_id"))[0]["point_id"]
        indications = Indication.objects.filter(start__gt=start, end__lt=end,
                                                point_id=id).values()  # получение данных по заданным параметрам

        indications_serialized = []  # сериализованный список словарей с нужными данными
        count_dict = {}  # словарь с количеством вхождений одинаковых датчиков в точке. Для подсчета среднего арифметического

        for i in indications:
            count = 1  # счетчик количества вхождений
            name = list(Sensor.objects.filter(id=i["sensor_id"]).values("name"))[0]["name"]
            unit = list(Sensor.objects.filter(id=i["sensor_id"]).values("unit"))[0]["unit"]

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

        for serial in indications_serialized:  # записываем значения уровней в зависимости от среднего арифметического
            for val in STATUS:
                if serial["name"] == val and serial["value"] > STATUS[val][0] and serial["value"] < STATUS[val][1]:
                    serial["status"] = "warning"
                elif serial["name"] == val and serial["value"] >= STATUS[val][1]:
                    serial["status"] = "critical"

        data = {
            "sensorReadings": indications_serialized
        }
        return JsonResponse(data)