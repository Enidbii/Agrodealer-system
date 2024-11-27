import json

from django.db.models import Q, F
import requests
from django.http import JsonResponse

from Agrostore.backend.utils import get_request_data
from Agrostore.backend.authenticate import get_employee, Corporate

class Querying(object):
    def query_employees(self, request):
        try:
            corporate = Corporate().read_a_corporate(request)
            print(corporate)
            data_field = corporate.get("data", {}).get("data")
            print(data_field)
            if data_field:
                try:
                    deserialized_data = json.loads(data_field)
                    print(deserialized_data)
                except json.JSONDecodeError:
                    deserialized_data = []
                    print("Error: Unable to parse stringified JSON array.")
            # filtered_store = [store for store in corporates1[1] if store['id'].]
            #q1 = Q(corporates1[name)
            # employees = get_employee()
            # print(employees)
            # q2 = Q(name=corporates1[0][0][2])
            # print(q2)
            return corporate

        except Exception as e:
            print(e)
            JsonResponse({"code": "403.000.000", "error": e})
