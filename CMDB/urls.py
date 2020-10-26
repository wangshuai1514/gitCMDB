from django.contrib import admin
from django.urls import path, include

from CMDB import views

urlpatterns = [
    path('CMDB/',views.do_scanhosts,name='scanhots'),
]