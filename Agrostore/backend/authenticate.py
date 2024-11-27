import json

import requests
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from Agrostore.models import Product, Supplier, Customer, Sale, SaleItem, Inventory, Task
from Agrostore.backend.servibase import ServiceInterface
from Agrostore.backend.utils import get_request_data, missing_required_fields


def auth_corp(token):
    if token:
        return True
    else:
        return False
def get_employee():
    resp = requests.get('http://127.0.0.1:8000/api/auth/retrieve-records/')
    print(resp.json())
    return resp.json()
class UserRequestInterface(object):
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/api/auth"
    def make_request(self, endpoint, **data):
        url = f"{self.base_url}/{endpoint}"
        resp = requests.post(url=url, json=data, verify=False)
        return resp.json()

class UserConnect(UserRequestInterface):
    def register(self, request):
        data = get_request_data(request)
        print(data)
        try:
            # requests.post('http://127.0.0.1:8000/api/auth/register/',data=json.dumps(data))
            self.make_request(endpoint='register/', **data)
            # self.make_request(endpoint='register/', **data)
            return JsonResponse({"code": "200.000", "message": "Employee created successfully"})

        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "could not create an employee"})

    def login(self, request):
        data = get_request_data(request)

        try:
            requests.get('http://127.0.0.1:8000/api/auth/login/', data=json.dumps(data))
            return JsonResponse({"code": "200.000.000", "message": "Employee logged in successfully"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Could not log in"})

    def update(self, request):
        data = get_request_data(request)

        try:
            requests.put('http://127.0.0.1:8000/api/auth/update/', data=json.dumps(data))
            return JsonResponse({"code": "200.000.000", "message": "Successfully updated a User!!"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Could not update you"})

    def delete_user(self, request):
        data = get_request_data(request)
        print(data)

        try:
            requests.get('http://127.0.0.1:8000/api/auth/delete/', data=json.dumps(data))
            return JsonResponse({"code": "200.000.000", "message": "User deleted successfully!!"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "User could not be deleted"})

    def read_a_user(self, request):
        data = get_request_data(request)
        print(data)
        try:
            response = requests.get('http://127.0.0.1:8000/api/auth/read-user/', data=json.dumps(data))
            data_dict = response.json()
            return JsonResponse({"code": "200.000.000", "data":data_dict})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "User does not exist"})

    def logout(self, request):
        pass

    def add_state(self, request):
        data = get_request_data(request)
        print(data)

        try:
            requests.post('http://127.0.0.1:8000/api/auth/add_state/', data=json.dumps(data))
            return JsonResponse({"code": "200.000.000", "message": "State added"})
        except Exception as e:
            print(e)
            return  JsonResponse({"code": "403.000.000", "message": "State not added!!"})

    def get_records(self, request):
        try:
            requests.get('http://127.0.0.1:8000/api/auth/retrieve-records/')
            return JsonResponse({"code": "200", "message": "success"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403", "message": "failed"})

    def auth_corp(self, request):
        data = get_request_data(request)
        print(data)

        try:
            response = requests.get('http://127.0.0.1:8000/api/auth/auth-check/', data=json.dumps(data))
            response_dict = response.json()
            token = response_dict["data"]
            print(token)
            if auth_corp(token):
                return JsonResponse({"code": "200", "message": "Access Granted"})
            else:
                return JsonResponse({"code": "403", "message": "Access denied"})

        except Exception as e:
            print(e)
            return JsonResponse({"code": "404", "message": "Enter correct token"})
class Tasking(object):
    def create_task(self, request):
        data = get_request_data(request)
        title = data.get('title')
        description = data.get('Description')
        status = data.get('status')
        priority = data.get('priority')
        sale_item_id = data.get('sale_item_id')

        req_fields = ['status', 'sale_item_id']
        if missing_required_fields(data, req_fields):
            return JsonResponse({"code": "404.000", "message": "Missing the required fields"})

        try:
            employee = get_employee()
            # print(employee)
            ServiceInterface().create(Task, title=title,description=description,status=status, priority=priority,
                                      sale_item_id=sale_item_id, employee = employee[2]['first_name'])
            return JsonResponse({"code": "200.000", "message": "Success"})
        except Exception as e:
            print(e)
            return None

    def read_tasks(self, request):
        try:
            tasks = ServiceInterface().retrieve_all_records(Task)
            queryset = tasks.values()
            print(queryset)
            data = json.dumps(list(queryset), cls=DjangoJSONEncoder)
            return JsonResponse({"code": "200.000", "data": data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Failed"})

    def update_task(self, request):
        data = get_request_data(request)
        title = data.get('title')
        description = data.get('description')
        status = data.get('status')
        priority = data.get('priority')
        sale_item_id = data.get('sale_item_id')
        tasks = Task.objects.get(title=title)
        print(tasks.id)

        try:
            update = ServiceInterface().update(Task, instance_id=tasks.id, title=title, description=description, status=status, priority=priority,
                                      sale_item_id=sale_item_id)
            #update.save()
            return JsonResponse({"code": "200.000", "message": "Successfully updated this task"})

        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000", "message": "Could  not update this task"})

    def delete_task(self, request):
        data = get_request_data(request)
        title = data.get('title')
        task = Task.objects.get(title=title)
        print(task.id)

        try:
            ServiceInterface().delete(Task, instance_id=task.id)
            return JsonResponse({"code": "200.000.000", "message": "Successfully deleted a task!!!!"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Could not delete this task"})

class Corporate(object):
    def create_corporate(self, request):
        data = get_request_data(request)
        print(data)

        try:
            requests.post('http://127.0.0.1:8000/api/auth/create_corporate/', data=json.dumps(data))
            return JsonResponse({"code": "200.000.000", "data": "Corporate created successfully"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Corporate not created"})

    def read_corporate(self, request):
        try:
            response = requests.get('http://127.0.0.1:8000/api/auth/read-corporates/')
            data_dict = response.json()
            return JsonResponse({"code": "200.000.000", "data": data_dict})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Could not return corporates"})

    def read_a_corporate(self, request):
        data = get_request_data(request)

        try:
            response = requests.get('http://127.0.0.1:8000/api/auth/read-one-corporate/', data=json.dumps(data))
            data_dict = response.json()
            return JsonResponse({"code": "200.000.000", "data": data_dict})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Could not return corporates"})


    def update_corporate(self, request):
        data = get_request_data(request)
        print(data)

        try:
            requests.post('http://127.0.0.1:8000/api/auth/corporate_update/', data=json.dumps(data))
            return JsonResponse({"code": "200.000.000", "message": "Corporate updated"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Corporate not updated"})

    def delete_corporate(self, request):
        data = get_request_data(request)
        print(data)

        try:
            requests.delete('http://127.0.0.1:8000/api/auth/delete-corporate/', data=json.dumps(data))
            return JsonResponse({"code": "200.000.000", "message": "Corporate deleted"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Corporate not deleted"})

class AgroStore(object):
    def add_product(self, request):
        data = get_request_data(request)
        product_name =data.get("product_name")
        category = data.get("category")
        unit_price = data.get("unit_price")

        required_fields = ['product_name', 'category', 'unit_price']
        if missing_required_fields(data, required_fields):
            return JsonResponse({"code": "404.000.000", "message": "You are missing some required fields!!"})

        try:
            product = ServiceInterface().create(Product, product_name=product_name, category=category,
                                                     unit_price=unit_price)
            product.save()

            return JsonResponse({"code": "200.000.000", "message": "Successfully added a product!"})
        except Exception as e:
            print(e)
            return None

    def create_supplier(self, request):
        data = get_request_data(request)
        supplier_name = data.get("supplier_name")
        contact = data.get("contact")
        address = data.get("address")

        required_fields = ['supplier_name', 'contact', 'address']
        if missing_required_fields(data, required_fields):
            return JsonResponse({"code": "404.000.000", "message": "Missing some required fields!!"})
        try:

            supplier = ServiceInterface().create(Supplier, supplier_name=supplier_name, contact=contact,
                                                      address=address)
            supplier.save()
            return JsonResponse({"code": "200.000.000", "message": "Successfully added a supplier!!"})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "403.000.000", "message": "Supplier was not added"})

    def create_customer(self, request):
        data = get_request_data(request)
        customer_name = data.get("customer_name")
        phone_number = data.get("phone_number")
        email = data.get("email")
        address = data.get("address")

        r_fields = ['customer_name', 'phone_number', 'email', 'address']
        if missing_required_fields(data, r_fields):
            return JsonResponse({"code": "404.000.000", "message": "Missing required fields"})
        try:
            customer = ServiceInterface().create(Customer, customer_name=customer_name, phone_number=phone_number,
                                                      email=email, address=address)
            customer.save()
            return JsonResponse({"code": "200.000.000", "message": "Customer created successfully!!"})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "403.000.000", "message": "Customer not created"})

    def create_sale(self, request):
        data = get_request_data(request)
        total_amount = data.get("total_amount")
        req_fields = ['total_amount']

        if missing_required_fields(data, req_fields):
            return JsonResponse({"code": '404.000.000', "message": "You have not entered the total amount"})

        try:
            sale = ServiceInterface().create(Sale, total_amount=total_amount)
            sale.save()
            return JsonResponse({"code": "200.000.000", "message": "Total amount entered successfully"})

        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "The entry failed"})

    def create_saleItem(self, request):
        data = get_request_data(request)
        quantity = data.get('Quantity')
        unit_price = data.get('unit_price')
        total_price = data.get('Total_price')
        req_fields = ['quantity', 'unit_price', 'total_price']

        if missing_required_fields(data, req_fields):
            return JsonResponse({"code": "404.000.000", "message": "Check your entry again, missing some fields"})

        try:
            sale_item = ServiceInterface().create(SaleItem, quantity=quantity, unit_price=unit_price, total_price=total_price)
            sale_item.save()
            return JsonResponse({"code": "200.000.000", "message": "Successfully created a sale item!!"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Could not create a sale item"})

    def create_inventory(self, request):
        data = get_request_data(request)
        quantity = data.get('Quantity')
        reason = data.get('Reason')

        req_fields = ['Quantity', 'Reason']
        if missing_required_fields(data, req_fields):
            return JsonResponse({"code": "403.000.000", "message": "Missing some required fields"})

        try:
            inventory = ServiceInterface().create(Inventory, quantity=quantity, reason=reason)
            inventory.save()
            return JsonResponse({"code": "200.000.000", "message":"Inventory created successfully"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Could not create an inventory"})

    # def create_employee(self, request):
    #     data = get_request_data(request)
    #     position = data.get("position")
    #     salary = data.get("salary")
    #     hire_date = data.get("hire_date")
    #     required_fields = ['first_name', 'last_name', 'email', 'username', 'password', 'phone_number',
    #                        'position', 'salary', 'hire_date']
    #
    #     if missing_required_fields(data, required_fields):
    #         return {"code": "404.000", "message": "You are missing some required fields"}
    #     else:
    #         try:
    #             user = ServiceInterface().create(Employee, position=position,
    #                                              salary=salary, hire_date=hire_date)
    #             user.save()
    #             print(user.id)
    #             return JsonResponse({"code": "200.000", "message": "User successfully created"})
    #         except Exception as e:
    #             print(e)
    #             return {"code": "404.000.000", "message": "User already exists"}