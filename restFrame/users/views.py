
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from .serializers import RegisterSerializer
from .models import *


def serialize_user(user):
    return {
        "id":user.id,
        "username": user.username,
        "email": user.email,
    }

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    created, token = AuthToken.objects.create(user )
    
    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email    
        },
        'token':token
    })
#read    
# @api_view(['GET'])
# def home_api(request):
#     detail_obj = Details.objects.all()
#     serializer = RegisterSerializer(detail_obj,many=True)  
#     return Response(serializer.data)

# @api_view(['POST'])
# def update_user_data(request,id):
#     detail_obj = Details.objects.get(id=id)
#     serializer = RegisterSerializer(instance =detail_obj,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def delete_user_data(request,id):
#     detail_obj = Details.objects.get(id=id)
#     detail_obj.delete() 
#     return Response("user is deleted") 
@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
           'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email    
             },
        })
    return Response({'error':'not authenticated'},status=400)

        
    
@api_view(['POST'])
def register_api(request):
    user_data = User.objects.all()
    required_fields = ["username", "email", "password"]
    serializer = RegisterSerializer(data=request.data)
    try:
       if serializer.is_valid(raise_exception=True):
          user = serializer.save()
          created, token = AuthToken.objects.create(user)
    
          return Response({'user_data': serialize_user(user),
                           'token':token,
                           'message':"User successfully registered",
                           'status':'success'})
    except Exception as e: 
        user_data = request.POST.get('username')
        existing_user = User.objects.filter(username='username').first()
        return Response({"status":"error",
                         "code": "USERNAME_EXISTS",
                         "message": "The provided username is already taken. Please choose a different username."
             })
    #    return Response({  
    #         "message": str(e),
    #         "code": "INTERNAL_SERVER_ERROR",
    #         "message": "An internal server error occured while registering the use. Please try again later"
    #     })    
