from urllib import response
import requests
import random
from django.conf import settings
def send_otp_phone(phone_number):
    try:
        otp = random.randint(1000,9999)
        url = f'https://2factor.in/API/V1/:{settings.API_KEY}/SMS/:phone_number/:otp_value/:otp_template_name'
        response =requests.get(url)
        return otp

    except Exception as e:
        return None

# curl --location --request GET 'https://2factor.in/API/V1/XXXX-XXXX-XXXX-XXXX-XXXX/SMS/+919999999999/12345/OTP1'

