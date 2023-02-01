from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.employee.api.api import EmployeesViewSet,EmployeesTypeViewSet

router= DefaultRouter()

router.register(r'addemployees',EmployeesViewSet, basename="addemployees")
router.register(r'addemployeesType',EmployeesTypeViewSet, basename="addemployeesType")

urlpatterns = [
    path('', include(router.urls)),
]