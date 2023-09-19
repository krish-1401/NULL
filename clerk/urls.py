from . import views
from django.urls import path
app_name='clerk'
urlpatterns = [
    path('',views.main,name='main'),
    path('register/',views.registerClerk,name='registerClerk'),
    path('login/',views.loginClerk,name='loginClerk'),
    path('dashboard/',views.dashboard,name='dashboard')
]