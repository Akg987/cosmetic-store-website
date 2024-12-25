from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage' ),
    path('profile', views.profile, name='profile' ),
    path('Create',views.createcosmetic,name='createcosmetic'),
    path('readallcosmetics/', views.readallcosmetics,name = "readallcosmetics"),
    path('productdetails/<int:id>/', views.productdetails,name = "productdetails"),
    path('productdetails/<int:id>/saveAsk', views.saveAsk,name = "saveAsk"),
    path('readallAsk/<int:id>', views.readallAsk,name = "readAsk"),
]