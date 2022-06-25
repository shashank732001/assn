from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name='home' ),
    path('login/',views.login,name='login' ),
    path('logout/',views.logout,name='logout' ),
    path('register/',views.register,name='register' ),


    #form pages
    path('add/',views.addcity,name='add-city'),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    ]