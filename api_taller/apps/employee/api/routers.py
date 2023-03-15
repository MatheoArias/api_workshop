from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.employee.api.api import EmployeesViewSet,EmployeesTypeViewSet

router= DefaultRouter()

router.register(r'add_employees',EmployeesViewSet, basename="add_employees")
router.register(r'add_employees_type',EmployeesTypeViewSet, basename="add_employees_type")

urlpatterns = [
    path('', include(router.urls)),
]