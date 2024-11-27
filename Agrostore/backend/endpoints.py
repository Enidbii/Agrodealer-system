from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from Agrostore.backend.authenticate import AgroStore, UserConnect, Tasking, Corporate
from Agrostore.backend.datatables import Querying


@csrf_exempt
def register(request):
    try:
        return HttpResponse(UserConnect().register(request))
    except Exception as e:
        print(e)
        return None
#
@csrf_exempt
def login(request):
    try:
        return HttpResponse(UserConnect().login(request))
    except Exception as ex:
        print(ex)
        return None
#
@csrf_exempt
def update_user(request):
    try:
        return HttpResponse(UserConnect().update(request))
    except Exception as ex:
        print(ex)
        return None

@csrf_exempt
def delete_user(request):
    try:
        return HttpResponse(UserConnect().delete_user(request))
    except Exception as e:
        print(e)
        return None
@csrf_exempt
def create_corporate(request):
    try:
        return HttpResponse(Corporate().create_corporate(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def corporate_update(request):
    try:
        return HttpResponse(Corporate().update_corporate(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def add_state(request):
    try:
        return HttpResponse(UserConnect().add_state(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def get_employees(request):
    try:
        return HttpResponse(UserConnect().get_records(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def get_an_employee(request):
    try:
        return HttpResponse(UserConnect().read_a_user(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def add_product(request):
    try:
        return HttpResponse(AgroStore().add_product(request))
    except Exception as ex:
        print(ex)
        return None

@csrf_exempt
def add_supplier(request):
    try:
        return HttpResponse(AgroStore().create_supplier(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def add_customer(request):
    try:
        return HttpResponse(AgroStore().create_customer(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def add_sale(request):
    try:
        return HttpResponse(AgroStore().create_sale(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def add_saleitem(request):
    try:
        return HttpResponse(AgroStore().create_saleItem(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def add_inventory(request):
    try:
        return HttpResponse(AgroStore().create_inventory(request))
    except Exception as e:
        print(e)
        return None
# @csrf_exempt
# def add_employee(request):
#     try:
#         return HttpResponse(AgroStore().create_employee(request))
#     except Exception as e:
#         print(e)
#         return None

@csrf_exempt
def auth_corp(request):
    try:
        return HttpResponse(UserConnect().auth_corp(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def create_task(request):
    try:
        return HttpResponse(Tasking().create_task(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def read_tasks(request):
    try:
        return HttpResponse(Tasking().read_tasks(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def update_task(request):
    try:
        return HttpResponse(Tasking().update_task(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def delete_task(request):
    try:
        return HttpResponse(Tasking().delete_task(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def read_corporates(request):
    try:
        return HttpResponse(Corporate().read_corporate(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def delete_corporate(request):
    try:
        return HttpResponse(Corporate().delete_corporate(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def read_one_corporate(request):
    try:
        return HttpResponse(Corporate().read_a_corporate(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def query_employees(request):
    try:
        return HttpResponse(Querying().query_employees(request))
    except Exception as e:
        print(e)
        return None





from django.urls import path

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("update_user/", update_user, name="update_user"),
    path("delete_user/", delete_user, name="delete_user"),
    path('create-corporate/', create_corporate, name="create_corporate"),
    path('corporate-update/', corporate_update, name="corporate_update"),#yet to test it
    path('read-corporates/', read_corporates, name="read_corporates"),
    path('delete-corporate/', delete_corporate, name="delete_corporate"),
    path("read-one-corporate/", read_one_corporate, name="read_one_corporate"),
    path("add_state/", add_state, name="add_sate"),
    path("add_product/", add_product, name="add_product"),
    path("add_supplier/", add_supplier, name="add_supplier"),
    path("add_customer/", add_customer, name="add_customer"),
    path("add_sale/", add_sale, name="add_sale"),
    path("add_saleitem/", add_saleitem, name="add_saleitem"),
    path("add_inventory/", add_inventory, name="add_inventory"),
    path("get-employees/", get_employees, name="get_employees"),
    path("auth-corp/", auth_corp, name="auth_corp"),
    path("create-task/", create_task, name="create-task"),
    path("read-tasks/", read_tasks, name="read_tasks"),
    path("update-tasks/", update_task, name="update_task"),
    path("delete-task/", delete_task, name="delete_task"),
    path("get-an-employee/", get_an_employee, name="get_employees"),
    path("get-corporate-employees/", query_employees, name='get_employees')
]