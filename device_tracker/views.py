from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import *
from .serializers import *

from django.contrib.auth import authenticate
from django.http import HttpResponse
from datetime import datetime

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# this is where registration hits.you write user password and company name as values
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

#hit this endpoint to get all employees or add an employeee
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
    

#hit this endpoint to get all devices or add an device for the specific company
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


#when a device is checkout this will be saved as the device log 
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deviceCheckout(request,empId,devId):
    
    device=Device.objects.get(id=devId)
    employee=Employee.objects.get(id=empId)
    checkout_condition=request.data.get("condition")
    
    if device.availability==True:

        device_log=DeviceLog.objects.create(device=device,employee=employee,checkout_date=datetime.now(),checkout_condition=checkout_condition )
        device.availability=False
        device.save()
        return Response("Ok",status.HTTP_201_CREATED)
    else:
        return Response("Device not available")



#when a device is return this will be saved as the device log 
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deviceReturn(request,logId):
    device_log=DeviceLog.objects.get(id=logId)
    device_log.device.availability=True
    device_log.return_date=datetime.now()
    device_log.return_condition=request.data.get("condition")

    device_log.save()
    

    return Response("Ok",status.HTTP_201_CREATED)
