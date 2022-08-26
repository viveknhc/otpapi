
from django.contrib import admin
from django.urls import path
from web.views import*
urlpatterns = [
    path('send_otp/',send_otp)
    path('admin/', admin.site.urls),
]
