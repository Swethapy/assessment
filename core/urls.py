from django.urls import path
from .views import index, dashboard

app_name = 'core'

urlpatterns = [
    # core/index/
    path('index/', index, name='index'),
    
    # core/employees
    path('employees/', dashboard, name='employees'),
]
