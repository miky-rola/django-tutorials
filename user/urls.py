from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import TaskViewset

router = DefaultRouter
router(r"", TaskViewset, name="task")
urlpatterns = [
    path("", include(router.urls))
]

