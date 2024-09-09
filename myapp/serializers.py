from rest_framework import serializers
from .models import CustomUser
from datetime import date, timedelta


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'birthdate']
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def check_bd(self, value):
        if value > date.today() - timedelta(days=16 * 365):
            raise serializers.ValidationError("Birthdate cannot be in the future.")
        return value