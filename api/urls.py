from django.urls import path, include
from .views import EmployeesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employees', EmployeesViewSet)

app_name = 'api'

urlpatterns = [
    # api/employees/
    path('', include(router.urls)),
]
