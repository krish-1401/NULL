from . import views
from django.urls import path
app_name='investor'
urlpatterns = [
    path('',views.main,name='main'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
]