from django.urls import path
from .views import *
urlpatterns = [
    path('register/',register_user),
    path('login/',loginView),
    path('logout/',logoutView),

    path('employee/',employeeAll),
    path('device/',deviceAll),
    path('device/<int:empId>/<int:devId>',deviceCheckout),
    path('device_return/<int:logId>',deviceReturn),

]