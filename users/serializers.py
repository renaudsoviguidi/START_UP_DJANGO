from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ["id", "email", "name", "password"]

    def create(self, validated_data):
        user = Users.objects.create(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user