# examples/views/department_views.py
from typing import List

from django.core.exceptions import ObjectDoesNotExist
from ninja import NinjaAPI
from ninja_crud import views, viewsets
from todo.models import Todo
from todo.schemas import TodoIn, TodoOut


api = NinjaAPI()


class TodoViewSet(viewsets.APIViewSet):
    api = api
    model = Todo
    list = views.ListView(response_body=List[TodoOut])
    create = views.CreateView(request_body=TodoIn, response_body=TodoOut)
    read = views.ReadView(response_body=TodoOut)
    update = views.UpdateView(request_body=TodoIn, response_body=TodoOut)
    delete = views.DeleteView()


@api.exception_handler(ObjectDoesNotExist)
def handle_object_does_not_exist(request, exc):
    return api.create_response(
        request,
        {"message": "Object not found"},
        status=404,
    )