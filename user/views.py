# from django.shortcuts import render

# # Create your views here.
# from .models import User

# user=User.objects.create(
#     name="miky",
#     email="test@email.com",
#     age=1
# )
# user=User(
#     name="andoh",
#     email="test2@email.com",
#     age=3
# )
# user, created =User.objects.get_or_create(
#     name="Delvin",
#     email="test3@email.com",
#     age=4
# )
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import TaskSerializer
from .models import Task


class TaskViewset(ModelViewSet):
    queryset = Task.objects.all().order_by("created_at")
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    http_method_names = ["get", "post", "put", "delete"]