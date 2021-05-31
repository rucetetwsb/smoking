from django.urls import path
from . import views

app_name = 'smoking'

urlpatterns=[
    path('boroughlist/', views.boroughlist, name='borough_list'),
    path('', views.smokingmap, name='smoking_map'),
    path('location/', views.location, name='location'),
    path('cp_cd/', views.cp_cd, name='cp_cd'),
    path('graph/', views.graph, name='graph'),
    path('direction/', views.direction, name='direction'),
    path('songpa_map/', views.songpa_map, name='songpa_map'),
]