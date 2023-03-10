from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','name','last_name','is_active','is_staff','is_superuser','last_login','groups','user_permissions']
        
class UsersSerializers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'
        
    def ro_representation(self,instance):
        return{
            'id':instance['id'],
            'username':instance['username'],
            'email':instance['email'],
            'password':instance['password'],
        }
