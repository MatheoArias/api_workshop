from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.users.api.api import UsersViewSets,CustomerUsersViewSets

router= DefaultRouter()
router.register(r'add_user',UsersViewSets, basename="add_user")
router.register(r'customer_user',CustomerUsersViewSets,basename="customer_user")

urlpatterns = [
    path('', include(router.urls)),
]