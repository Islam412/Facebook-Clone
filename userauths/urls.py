from django.urls import path
from userauths import views


app_name = 'userauths'


urlpatterns = [
    path('sign-up/', views.RegisterView, name='sign-up'),
    path('sign-in/', views.LoginView, name='sign-in'),
    path('user/sign-out/', views.LogoutView, name='sign-out'),
    path('user/my-profile/', views.my_profile, name='my-profile'),
]
