from rest_framework import serializers
from .models import CustomUsers
class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUsers
        fields=['username','first_name','last_name','email','password']
    
    def create(self, validated_data):
        user = super(User_Serializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user