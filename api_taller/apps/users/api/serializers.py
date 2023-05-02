from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','name','last_name','is_active','is_staff','is_superuser','last_login','groups','user_permissions']
        
class UsersSerializers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'
        
    def update(self,instace,validated_data):
        updated_user=super().update(instace,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
        
    def create(self,validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def ro_representation(self,instance):
        return{
            'id':instance['id'],
            'email':instance['email'],
            'password':instance['password'],
        }
