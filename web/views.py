from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .helpers import send_otp_phone
from .models import User
# Create your views here.

def send_otp(request):
    data =request.data

    if data.get('phone_number') is None:
        return Response({
            'satus':400,
            'message':'key phone number is required'
        })

    if data.get('password') is None:
        return Response({
            'satus':400,
            'message':'key phone number is required'
        })

    user = User.objects.create(
        phone_number= data.get('phone_number'),
        otp = send_otp_phone(data.get('phone_number'))
        )
    user.set_password = data.get('set_password')
    user.save()

    return Response({
        'status': 200 , 'message' : 'Otp sent'
    })
