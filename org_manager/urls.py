from django.urls import path

from .views import ManagerViewset, EmployeeViewset

from rest_framework import routers
router = routers.DefaultRouter()

router.register('manager', ManagerViewset, basename='manager'),
router.register('employee', EmployeeViewset, basename='employee')


urlpatterns = [
   *router.urls
]

