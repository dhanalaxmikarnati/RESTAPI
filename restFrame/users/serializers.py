from django.contrib.auth.models import User
from rest_framework import serializers,validators
from .models import  *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs={
                "password":{"write_only":True},
                "email":{
                "required":True,
                "allow_blank":False,
                "validators":{
                    validators.UniqueValidator(
                        User.objects.all(),"A user with that email already exists"
                    )
                }
                
            }
        }    

def create(self, validated_data):
    username = validated_data.get('username')
    password = validated_data.get('password')
    email = validated_data.get('email')
    firstname = validated_data.get('firstname')
    lastname = validated_data.get('lastname')
    
    user = User.objects.create(
        username=username,
        password=password,
        email=email,
        firstname=firstname,
        lastname=lastname
    )
    
    return user

