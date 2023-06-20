from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import *
from .serializers import *

from django.contrib.auth import authenticate

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    company_name = request.data.get('company_name') 
    print(f"{username} is {password} and then {company_name}")

    if username and password and company_name:
        user = User.objects.create_user(username=username, password=password)
        Company.objects.create(user=user, name=company_name)        
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'message': 'Missing required data.'}, status=400)



@api_view(['POST'])
def loginView(request):
    
    username = request.data.get('username')
    password = request.data.get('password')

    print(f"{username} is {password} ")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=401)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 
def logoutView(request):
   
    token = Token.objects.get(user=request.user)
    
    
    token.delete()
    return Response({'message': 'Logged out successfully'})  




@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 
def test(request):
   return Response("Authenticated endpoint")    



@api_view(['POST','GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def employeeAll(request):
        if request.method=="GET":
            employees=Employee.objects.filter(company=request.user.company)
            
            employees_json=EmployeeSerializer(employees,many=True)
            return Response(employees_json.data )
    
        if request.method=="POST":
            name=request.data.get("name")
            company=request.user.company.id
            data={'company':company,'name':name}
            serializer=EmployeeSerializer(data=data)
            print(serializer.initial_data)

            if serializer.is_valid():
                serializer.save()
                return Response({'msg':"successfully created"},status.HTTP_201_CREATED)
            else:
                return Response({"error":serializer.errors})
    
@api_view(['POST','GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deviceAll(request):
        if request.method=="GET":
            devices=Device.objects.filter(company=request.user.company,availability=True)
            
            device_json=EmployeeSerializer(devices,many=True)
            return Response(device_json.data )
    
        if request.method=="POST":
            name=request.data.get("name")
            company=request.user.company.id
            data={'company':company,'name':name}
            serializer=DeviceSerializer(data=data)
            print(serializer.initial_data)

            if serializer.is_valid():
                serializer.save()
                return Response({'msg':"successfully created"},status.HTTP_201_CREATED)
            else:
                return Response({"error":serializer.errors})
    

