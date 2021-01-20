from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('solve/<int:quiz_id>/', views.solve, name='solve'),
    path('result/<int:quiz_id>/', views.result, name='result'),
    path('create/', views.create, name='create'),
]
