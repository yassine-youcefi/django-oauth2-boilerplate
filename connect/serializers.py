from rest_framework import serializers
from connect.models import User

class GetConnectUserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = [
            'id',
            'picture',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
        ]

 