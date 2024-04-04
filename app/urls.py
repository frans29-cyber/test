from django.urls import path
from .views import *
urlpatterns = [
    path('dash', home, name='dashboard'),
    path('', login_views, name='login_views'),
    path('second_password/', second_password, name='second_password'),
]
