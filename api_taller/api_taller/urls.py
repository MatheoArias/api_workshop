from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/',include('apps.employee.api.routers')),
    path('products/',include('apps.products.api.routers')),
    path('vehicles/',include('apps.vehicle.api.routers')),
    path('categories/',include('apps.category.api.routers')),
    path('customers/',include('apps.customer.api.routers')),
    path('bills/',include('apps.bill.api.routers')),
]
