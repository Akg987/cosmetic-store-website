from django.urls import path
from . import views

urlpatterns = [
    path('', views.logins, name='login' ),
    path('checkloginAjaxs/<str:UserName>/<str:Password>', views.checkloginAjaxs,name = "checklogin"),
    path('register', views.register,name = "home"),
    path('getCookies', views.getCookies,name = "home"),
    path('checklogin', views.checklogin,name = "home"),
    path('registerAction', views.registerAction,name = "home"),
    path('CheckAuth', views.CheckAuth,name = "CheckAuth"),
    path('LogOut', views.LogOut,name = "LogOut"),
]
