from django.urls import path
from .views import *
urlpatterns = [
    path('register/',register_user),
    path('login/',loginView),
    path('logout/',logout_view),
    path('test/',test),

]