from django.contrib import admin
#from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from knox import views as knox_views
from . import views


urlpatterns = [
    #path('',views.home_api),
    path('login/',views.login_api),
    path('user/',views.get_user),
    #path('update/<int:id>/',views.update_user_data),
    #path('delete/<int:id>/',views.delete_user_data),
    path('register/',views.register_api),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/',knox_views.LogoutAllView.as_view())
]