from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username','email', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Senha invalida')
        return data
    
    def create(self, data):
        data.pop('confirm_password')
        user = User.objects.create_user(**data)
            
        return user

    def update(self, instance, data):
        data.pop('confirm_password', None)
        password = data.pop('password', None)

        for attr, value in data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance