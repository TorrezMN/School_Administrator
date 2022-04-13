"""SChool_Admin_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path

from .views import Admin_Home
from .views import Admin_New_Employee

urlpatterns = [
    path('', Admin_Home.as_view(), name='admin_home'),

    # Employees
    path(r'nuevo_empleado',
         Admin_New_Employee.as_view(),
         name='admin_new_employee'),
]
