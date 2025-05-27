import json
from yourapp.serializers import CarSerializer
from yourapp.models import Car


def serialize_car_object(instance: Car):
    serializer = CarSerializer(instance)
    data = serializer.data
    return json.dumps(data)


def deserialize_car_object(data: dict):
    data_dict = json.loads(data)
    serializer = CarSerializer(data=data_dict)
    if serializer.is_valid():
        return serializer.save()
    return serializer.errors
