from .models import Trip
from django.contrib.auth import get_user_model
from rest_framework import serializers, fields
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 


class UserSerializer(serializers.ModelSerializer):
  password1 = serializers.CharField(write_only= True)
  password2 = serializers.CharField(write_only= True)

  def validate(self, data):
    print("*-----------data", data)
    if data['password1'] != data['password2']:
      raise serializers.ValidationError("Passwords must match")
    return data

  def create(self, validated_data):
    print("validated_data-------------",  validated_data)
    data = {
      key: value for key, value in validated_data.items() if key not in ('password1', 'password2')
    }
    data['password'] = validated_data['password1']
    return self.Meta.model.objects.create_user(**data)

  class Meta:
    model = get_user_model()
    fields = (
      'id', 'username', 'password1', 'password2',
      'first_name', 'last_name',
    )
    read_only_fields = ('id',)
  
class LogInSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    print("token------", token)
    user_data = UserSerializer(user).data
    print("user_data-------------", user_data )
    for key, value in user_data.items():
      if key != 'id':
        token[key] = value
    return token

class TripSerializer(serializers.ModelSerializer):
  class Meta:
    
    model = Trip
    fields = '__all__'
    read_only_fields = ('id', 'created', 'updated')

class NestedTripSerializer(serializers.ModelSerializer):
  #serializes the full Trip object
  class Meta:
    
    model = Trip
    fields = '__all__'
    depth = 1
    



