from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from apps.users.api.api import Login,Logout
from rest_auth.views import PasswordResetView,PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/',include('apps.employee.api.routers')),
    path('products/',include('apps.products.api.routers')),
    path('vehicles/',include('apps.vehicle.api.routers')),
    path('categories/',include('apps.category.api.routers')),
    path('customers/',include('apps.customer.api.routers')),
    path('bills/',include('apps.bill.api.routers')),
    path('users/',include('apps.users.api.routers')),
    path('login',Login.as_view(),name='login'),
    path('logout',Logout.as_view(),name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/fresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password/reset/', PasswordResetView.as_view(),name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
