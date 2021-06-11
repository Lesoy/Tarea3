from django.contrib import admin
from django.urls import path, include
from .views import index, patan, perros, garfield, gatos, scooby, coraje, doraemon, tom

urlpatterns = [
    path('',index,name='IND'),
    path('gatos/',gatos,name='GAT'),
    path('perros/',perros,name='PER'),
    path('patan/',patan,name='PAT'),
    path('garfield/',garfield,name='GAR'),
    path('scooby/',scooby,name='SCO'),
    path('coraje/',coraje,name='COR'),
    path('doraemon/',doraemon,name='DOR'),
    path('tom/',tom,name='TOM'),
]